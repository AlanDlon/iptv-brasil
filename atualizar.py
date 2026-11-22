from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen

FONTE = "https://iptv-org.github.io/iptv/countries/br.m3u"
DESTINO = Path(__file__).with_name("brasil.m3u")


def validar(conteudo):
    linhas = conteudo.decode("utf-8-sig").splitlines()
    if not linhas or linhas[0].split()[:1] != ["#EXTM3U"]:
        raise ValueError("A fonte não retornou uma playlist M3U.")
    pendente = False
    entradas = 0
    for linha in linhas[1:]:
        linha = linha.strip()
        if linha.startswith("#EXTINF:"):
            if pendente:
                raise ValueError("Entrada sem endereço de transmissão.")
            pendente = True
        elif linha and not linha.startswith("#"):
            if not pendente or "://" not in linha:
                raise ValueError("Endereço de transmissão inválido.")
            entradas += 1
            pendente = False
    if pendente or not entradas:
        raise ValueError("Playlist incompleta ou vazia.")
    return entradas


if __name__ == "__main__":
    with urlopen(FONTE, timeout=60) as resposta:
        conteudo = resposta.read()
    entradas = validar(conteudo)
    with TemporaryDirectory(dir=DESTINO.parent) as pasta:
        temporario = Path(pasta) / DESTINO.name
        temporario.write_bytes(conteudo)
        temporario.replace(DESTINO)
    print(f"Playlist atualizada com {entradas} entradas.")
