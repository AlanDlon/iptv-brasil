import csv
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen

FONTE = "https://iptv-org.github.io/iptv/countries/br.m3u"
PASTA = Path(__file__).resolve().parent
GRUPOS = ("TV aberta", "TV por assinatura")
ID = re.compile(r'\btvg-id="([^"]*)"')
GRUPO = re.compile(r'\bgroup-title="[^"]*"')


def carregar_catalogo():
    canais = {}
    with (PASTA / "canais.csv").open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            canal, grupo = linha["id"], linha["grupo"]
            if not canal or canal in canais or grupo not in GRUPOS:
                raise ValueError(f"Classificação inválida para {canal!r}")
            canais[canal] = grupo
    return canais


def filtrar(conteudo, catalogo):
    linhas = conteudo.decode("utf-8-sig").splitlines()
    if not linhas or linhas[0].split()[:1] != ["#EXTM3U"]:
        raise ValueError("A fonte não retornou uma playlist M3U.")

    grupos = {nome: [] for nome in GRUPOS}
    entrada = []
    for linha in linhas[1:]:
        if linha.startswith("#EXTINF:"):
            if entrada:
                raise ValueError("Entrada sem endereço de transmissão.")
            entrada = [linha]
        elif not linha.strip():
            continue
        elif linha.startswith("#"):
            if entrada:
                entrada.append(linha)
        else:
            if not entrada or "://" not in linha:
                raise ValueError("Endereço de transmissão inválido.")
            meta = entrada[0]
            identificador = ID.search(meta)
            canal = identificador[1].partition("@")[0] if identificador else ""
            grupo = catalogo.get(canal)
            if grupo:
                atributo = f'group-title="{grupo}"'
                if GRUPO.search(meta):
                    entrada[0] = GRUPO.sub(atributo, meta, count=1)
                else:
                    entrada[0] = meta.replace(",", f" {atributo},", 1)
                grupos[grupo].append([*entrada, linha])
            entrada = []
    if entrada or not all(grupos.values()):
        raise ValueError("Playlist incompleta ou sem entradas para um dos grupos.")
    saida = [linhas[0]]
    for nome, entradas in grupos.items():
        print(f"{nome}: {len(entradas)} sinais")
        for item in entradas:
            saida.extend(item)
    return ("\n".join(saida) + "\n").encode("utf-8")


if __name__ == "__main__":
    with urlopen(FONTE, timeout=60) as resposta:
        playlist = filtrar(resposta.read(), carregar_catalogo())
    with TemporaryDirectory(dir=PASTA) as pasta:
        temporario = Path(pasta) / "brasil.m3u"
        temporario.write_bytes(playlist)
        temporario.replace(PASTA / "brasil.m3u")
