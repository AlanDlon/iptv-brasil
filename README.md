# IPTV Brasil

Playlist de canais de TV aberta e por assinatura com sinal listado para o Brasil no iptv-org, incluindo afiliadas regionais. O player exibe dois grupos, **TV aberta** e **TV por assinatura**. Incluímos no primeiro grupo os canais também disponíveis por parabólica gratuita quando essa distribuição foi identificada.

## Assistir

Cole este endereço na opção de abrir um fluxo de rede do VLC ou no campo de playlist M3U do seu player.

```text
https://raw.githubusercontent.com/AlanDlon/iptv-brasil/main/brasil.m3u
```

## Premiere

Os jogos estão disponíveis para assinantes na [programação oficial do Premiere no Globoplay](https://globoplay.globo.com/canais/premiere/). Os sinais cadastrados entram na playlist M3U quando o iptv-org disponibiliza o respectivo endereço na lista do Brasil.

## Cobertura e atualização

A lista inclui todos os sinais em que o identificador do iptv-org corresponde a uma emissora do [catálogo de classificação](./canais.csv). Cada registro contém o grupo e a referência consultada. Rádios, canais exclusivos de streaming e entradas sem classificação ficam fora da playlist. Uma emissora pode ter vários sinais. A reprodução depende do endereço publicado pela fonte, da região e das condições de acesso da emissora.

O fluxo diário do GitHub Actions reaplica esse filtro. Para executar a mesma atualização localmente, use `python3 atualizar.py`. Para incluir uma nova emissora, acrescente ao catálogo seu identificador, o grupo e uma referência de distribuição no Brasil.

## Fonte

Consulte o [catálogo de playlists do iptv-org](https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md). Este projeto distribui uma lista de endereços. As transmissões são fornecidas pelos respectivos servidores.

[Contribua com meu trabalho](./contribua-com-meu-trabalho/)
