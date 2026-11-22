# IPTV Brasil

Playlist com todas as entradas da lista do Brasil mantida pelo [iptv-org](https://github.com/iptv-org/iptv). A seleção acompanha a classificação por país do projeto, incluindo variações regionais e sinais alternativos. A disponibilidade de cada transmissão depende da emissora e da região.

## Assistir

Abra o arquivo `brasil.m3u` no VLC. Para usar a versão mais recente diretamente da fonte, cole o endereço abaixo na opção de abrir um fluxo de rede.

```text
https://iptv-org.github.io/iptv/countries/br.m3u
```

Em um repositório público, você também pode abrir `brasil.m3u` no GitHub e copiar o endereço da versão **Raw** para o seu player.

## Atualizar

Execute `python3 atualizar.py` para baixar e validar a playlist. O script preserva os dados originais, incluindo nomes, categorias, logos e opções de reprodução.

No GitHub, com Actions habilitado e permissão de escrita na branch padrão, o fluxo **Atualizar canais brasileiros** verifica a fonte diariamente e grava mudanças. Para executá-lo manualmente, abra **Actions → Atualizar canais brasileiros → Run workflow**.

## Fonte

Consulte o [catálogo de playlists do iptv-org](https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md). Este projeto distribui uma lista de endereços. As transmissões são fornecidas pelos respectivos servidores.
