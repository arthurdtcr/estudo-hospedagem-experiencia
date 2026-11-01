Texto na tela do Reels: o gancho dos primeiros 2 segundos e a legenda da fala, sempre sobre `placa`.

- **Use quando:** em todo Reels. O gancho segura quem rola; a legenda serve quem assiste sem som.
- **Você fornece:** o gancho (até 6 palavras, em `gancho-video`, um `<em>`) e a fala, quebrada em blocos de até 2 linhas e cerca de 32 caracteres por linha, de 1,2 a 2,5 segundos cada.
- **Estrutura:** camada transparente 1080 × 1920 (`ie-arte ie-reels ie-transparente`, sem o `ie-video-vazio` e sem as guias) > `ie-area ie-entre` > `ie-placa gancho-video ie-serif` no topo e `ie-legenda legenda-video ie-sans` na base. A área já desconta `reels-topo`, `reels-base` e a coluna `reels-direita`.
- **O que o Claude entrega:** PNGs transparentes `NN-reels-gancho.png` e `NN-reels-legenda-MM.png` (um por bloco) e o roteiro com tempo de entrada e saída de cada um. O gancho entra no segundo 0 e sai no 2, sem animação além de corte seco.
- **Não faça:** texto sem placa sobre vídeo; legenda em `tinta-suave`; ligar a legenda automática do Instagram quando a fala já está queimada (fica duplicada).
