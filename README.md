# 📺 Tblack IPTV

Playlist M3U organizada para uso em players compatíveis com IPTV.

> **Playlist atual:** 68 entradas / 65 nomes de canais distintos.

## 🔗 URL da playlist

Use esta URL diretamente no seu aplicativo ou player IPTV:

```text
https://ewertonmendes.github.io/tblack-iptv/playlist.m3u
```

> O repositório precisa estar **público** para que a URL acima funcione sem autenticação.

## ▶️ Como usar

1. Abra o seu player IPTV.
2. Escolha a opção de adicionar uma playlist por **URL / M3U**.
3. Cole a URL da playlist.
4. Salve e aguarde o aplicativo carregar os canais.

Também é possível abrir o arquivo `playlist.m3u` diretamente em players que aceitam arquivos M3U.

## 📚 Guia de canais

<details>
<summary><strong>📡 TV aberta</strong> (5)</summary>

- Band
- Globo — fonte 1
- Globo — fonte 2
- Record
- SBT

</details>

<details>
<summary><strong>📰 Notícias</strong> (3)</summary>

- Band News
- CNN Brasil
- Globo News

</details>

<details>
<summary><strong>⚽ Esportes</strong> (18)</summary>

- BandSports
- Combate
- ESPN
- ESPN 2
- ESPN 3
- ESPN 4
- Premiere 2
- Premiere 3
- Premiere 4
- Premiere 5
- Premiere 6
- Premiere 7
- Premiere Clubes
- Sportv 1
- Sportv 2
- Sportv 3
- XSports
- XSPORTS

</details>

<details>
<summary><strong>🎬 Filmes & Séries</strong> (27)</summary>

- A&E
- AXN
- Cinemax
- HBO
- HBO 2
- HBO Family
- HBO Mundi
- HBO Plus
- HBO Pop
- HBO Xtreme
- Megapix
- Paramount Plus — fonte 1
- Paramount Plus — fonte 2
- Prime Video 1
- Prime Video 2
- Space
- Studio Universal — fonte 1
- Studio Universal — fonte 2
- Telecine Action
- Telecine Cult
- Telecine Fun
- Telecine Pipoca
- Telecine Premium
- Telecine Touch
- TNT
- Universal Channel
- Universal TV

</details>

<details>
<summary><strong>🧒 Infantil</strong> (4)</summary>

- Cartoon Network
- Cartoonito
- Discovery Kids
- Gloob

</details>

<details>
<summary><strong>🌎 Documentários & Lifestyle</strong> (8)</summary>

- Animal Planet
- Discovery Home & Health
- Discovery Channel
- Discovery Science
- Discovery Turbo
- H2
- HGTV
- History

</details>

<details>
<summary><strong>🎵 Entretenimento</strong> (3)</summary>

- Adult Swim
- MTV
- Multishow

</details>

## 🗓️ Guia de programação / EPG

A lista acima é apenas um **guia dos canais disponíveis**.

Para mostrar a programação por horário — por exemplo, o que está passando agora e os próximos programas — é necessário adicionar um arquivo **EPG/XMLTV**, normalmente chamado:

```text
epg.xml
```

Depois, a playlist ou o player pode ser configurado para relacionar cada `tvg-id` do M3U ao canal correspondente no EPG.

Atualmente este repositório contém apenas a playlist M3U.

## ℹ️ Observações

- A disponibilidade dos canais depende das URLs/fontes presentes na playlist.
- Alguns canais possuem mais de uma entrada por utilizarem fontes alternativas.
- Se uma fonte expirar ou ficar indisponível, o canal pode deixar de funcionar até a playlist ser atualizada.
- O arquivo principal utilizado pelos players é `playlist.m3u`.

## 📁 Estrutura sugerida

```text
tblack-iptv/
├── playlist.m3u
├── README.md
└── epg.xml        # opcional, caso seja adicionado um EPG futuramente
```

---

**Tblack IPTV**
