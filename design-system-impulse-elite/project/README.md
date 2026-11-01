Impulse Elite é a evolução do sistema preto e dourado da Impulse Performance para o Instagram: carrossel, estático, story, Reels e destaques. A paleta oficial continua a mesma. Muda a postura: menos cartaz, mais editorial. Serifa no lugar da condensada, ouro usado como assinatura e não como enfeite, muito espaço vazio.

## Essência

- **Silêncio antes de brilho.** O preto domina. O dourado aparece pouco e sempre no lugar que importa.
- **Uma ideia por arte.** Um gancho, uma ênfase, uma ação.
- **Ângulo do monograma.** O traço diagonal e o canto cortado da logo viram a forma da marca: `ie-diagonal` e o chanfro (`chanfro-sm`, `chanfro-lg`). Nada é arredondado.
- **Feito para o polegar.** A arte de 1080 aparece com cerca de 36% do tamanho no celular, no meio do feed, por um segundo. Se não se entende nesse tamanho, não está pronta.

## Como montar com este sistema

Siga esta ordem sempre que for criar uma peça. Ela vale para o Claude e para qualquer pessoa da equipe.

1. **Leia** este README e `tokens.json`. Para cada componente que for usar, leia `components/<Nome>/README.md` e copie a estrutura de `components/<Nome>/preview.html`. Não invente classe: se não está em `components/bundle.css`, não existe.
2. **Briefing.** Sem objetivo, formato, pilar, gancho e ação, não comece: complete pelo modelo de `Briefing.md` (pergunte o que faltar; o que não for respondido, assuma e diga que assumiu).
3. **Roteiro antes do desenho.** Escreva o texto slide a slide numa tabela (slide, composição, texto, por quê), com no máximo 40 palavras por slide, e mostre antes de montar.
4. **Escolha as composições** pelas regras de Variação. Para saber o que veio antes, leia o título dos três últimos canvases "Carrossel NN" (o registro do passo 6).
5. **Monte** num canvas do tipo Design: instale este sistema (`tokens.json` e `components/bundle.css`), compile as variáveis de `tokens.json` numa folha `tokens.css` (tema `noite` em `:root`, tema `marfim` em `[data-theme="marfim"]`, uma classe por estilo de texto) e ligue as duas folhas em cada artboard. Uma artboard por slide, no tamanho de Formatos, nomeada "N · função" ("1 · Capa", "4 · Pausa").
6. **Registre** na nota de título do canvas: "Série · NN · Título · Capa C? · Fechamento ? · Pausa sim/não · Objetivo". É o que o próximo post consulta.
7. **Revise** com o Checklist antes de publicar e escreva a legenda e o texto alternativo por `Legenda.md`.

## Voz e texto

- Seca, direta, humana. Frases curtas, finais com impacto, reticências para suspense ("E o caixa... no mesmo lugar.").
- Fala com o empresário em "você"; a Impulse fala em "a gente"; o fundador fala em "eu" só nos slides dele.
- Nunca use travessão. Use ponto, dois-pontos ou reticências.
- Sem superlativo, sem promessa que não se sustenta, sem número sem fonte. Se tem número, a fonte e o período aparecem ao lado em `nota`.
- No máximo 40 palavras por slide.
- Palavras do empresário: cliente, venda, caixa, atendimento, conversa. Jargão de agência (CPL, ROAS, funil, lead) só com a tradução na mesma frase.
- Exemplos reais: "Anúncio não vende nada sozinho." · "O anúncio só traz a pessoa até a porta." · "O primeiro passo é gratuito." · "Seu cliente não sumiu. Esfriou." Mais ganchos e ações em `Ganchos.md`.

## Cor

- Proporção: `fundo` cerca de 60%, `tinta` cerca de 25%, `destaque` no máximo 10%, o resto em `tinta-suave` e `filete`.
- Use sempre os tokens semânticos (`fundo`, `superficie`, `superficie-alta`, `tinta`, `tinta-suave`, `destaque`, `on-destaque`, `filete`, `placa`). As cores da paleta (`preto-impulse`, `marfim`, `dourado`…) só aparecem direto no degradê metálico, na capa de destaque e no brilho.
- `destaque` só em: rótulo, palavra em `<em>`, numeral, filete dourado, barra em foco, CTA. Nunca em parágrafo.
- Tema `noite` em quase tudo. Tema `marfim` na pausa (no máximo um slide por carrossel) e nas capas claras C4 e C6; lá o destaque vira `bronze`.
- Degradê metálico (`metal-text`, `ie-metal`): só em numeral e filete curto. As paradas são `ouro-escuro`, `ouro-medio`, `ouro-claro`, `champagne`, `ouro-medio`, `ouro-escuro`.
- Texto de apoio sobre marfim é `cinza-grafite`, nunca `cinza-texto` (não tem contraste).
- Cartão e balão em `superficie` levam sempre `filete` em volta: grafite sobre preto é 1.2:1 e some no celular.
- Sobre vídeo, texto só em cima de `placa`, e só em `tinta` ou `destaque`.
- **Modo escuro do app.** O `preto-impulse` se funde com a interface: a arte perde a borda e vira texto flutuando. Por isso a grade alterna capas claras e o texto sempre respeita as margens.

## Tipografia

- Duas famílias, ambas do Google Fonts: `serif` (Instrument Serif, com itálico) para manchetes e números; `sans` (Montserrat, a mesma geometria da palavra IMPULSE na logo) para texto e rótulos.
- Estilos para a arte em 1080 de largura: `capa` 176, `manchete` 120, `titulo` 84, `item` 56, `numeral` 280 na serifa; `lead` 40, `corpo` 34, `nota` 24, `rotulo` 22 na sans; no vídeo, `gancho-video` 104 (serifa) e `legenda-video` 44 (sans 600).
- Tudo que precisa ser lido fica em `corpo` (34px, cerca de 12pt no celular) ou maior. `nota` (24px) só para o que pode passar sem leitura: fonte, crédito, dica. `rotulo` (22px, caixa alta, `0.32em`, peso 600) é a única exceção abaixo de 24px.
- Serifa sempre em caixa normal, com ponto final. Ênfase em itálico `<em>`, uma por slide.
- Montserrat só nos pesos 400, 500 e 600.

## Formatos e zonas seguras

| Peça | Tamanho | Classe | Zona livre |
| --- | --- | --- | --- |
| Carrossel, estático | 1080 × 1350 (4:5) | `ie-arte` | `margem-x` 88, `margem-y` 112; a grade corta 34px de cada lado |
| Post 3:4 (opcional) | 1080 × 1440 | `ie-arte ie-34` | igual ao 4:5; preenche a grade sem corte, mas não vire anúncio |
| Story | 1080 × 1920 | `ie-arte ie-story` | 250 em cima, 340 embaixo |
| Reels (texto na tela) | 1080 × 1920 | `ie-arte ie-reels` | 250 em cima, 440 embaixo, 140 à direita |
| Capa de Reels | 1080 × 1920 | `ie-arte ie-capa-reels` | título entre y 336 e y 1480 (a grade corta 240 em cima e embaixo) |
| Capa de destaque | 1080 × 1080 | `ie-arte ie-quadrado` | círculo central |
| Story ou Reels como anúncio | 1080 × 1920 | | base livre sobe para 672 |

- O carrossel aceita até 20 slides; o sistema usa de 7 a 10. Todos os slides têm a proporção do primeiro.
- As medidas estão em `tokens.json` (família `formato`) e no componente `ZonasSeguras`. Elas mudam com o app: confira na prévia do Instagram antes de publicar.
- Exporte em PNG, 1080 de largura, sRGB, um arquivo por slide, nomeado `NN-slide-MM.png` (`15-slide-01.png`).

## Grid e respiro

- Texto ancorado: capa na base, slides internos com rótulo no topo e bloco na metade de baixo.
- Espaço entre blocos em `space-6` (48px); manchete e resto separados por `space-12` (96px) quando couber.
- Story: 1080 × 1920, área útil já descontada pela `ie-story`.

## Formas e textura

- `canto` é 0 em tudo. O único corte é o chanfro no canto superior direito, como o monograma: botões, cartões, balões, barras, selos, placas e fotos em moldura.
- `ie-grao` (opacidade `grao`) em toda arte Noite: dá textura de papel.
- `ie-brilho` (opacidade `brilho`) só na capa, no CTA, no estático, no story e na capa de Reels.
- `ie-diagonal`: no máximo uma por arte, cruzando a borda, longe do texto e do `ie-arraste`.
- `ie-arraste` em toda capa de carrossel: o filete sai pela borda direita. `ie-costura` no slide 2, quando a base esquerda está livre, recebe esse filete.
- Sem sombra, sem cartão com borda colorida na lateral, sem ícone decorativo, sem emoji.

## Fotografia e vídeo

- Pessoas sempre em preto e branco (`ie-retrato`): `grayscale(1)`, contraste 1.12, fundo escuro, luz lateral, recorte do peito para cima.
- A base da foto se dissolve no `fundo`. Foto que sangra a borda não leva chanfro; foto em moldura leva `chanfro-lg`.
- Nunca foto colorida, banco de imagem genérico ou pessoa sorrindo para a câmera sem contexto.
- **Reels:** gancho na tela nos dois primeiros segundos (`gancho-video` sobre `placa`), legenda da fala do começo ao fim (`legenda-video`), capa própria (`CapaReels`). O texto vem de uma camada PNG transparente montada com `ReelsTexto`.
- **Originalidade:** desde abril de 2026 o Instagram tira das recomendações as contas que mais repostam do que criam, também em foto e carrossel. Tudo aqui é gravado, escrito e desenhado pela Impulse; trecho de terceiro só com comentário por cima e crédito.

## Componentes

Cada componente tem uma prévia viva e um README com quando usar, o que fornecer, a estrutura e o que não fazer.

- **Capas (7):** C1 `CarrosselCapa` (Base) · C2 `CapaPalavra` · C3 `CapaNumero` · C4 `CapaDividida` · C5 `CapaMoldura` · C6 `CapaMarfim` · C7 `CapaRosto`.
- **Miolo (14):** `CarrosselTexto` · `MioloDeclaracao` · `CarrosselLista` · `MioloGrade` · `MioloChecklist` · `MioloContraste` · `MioloConversa` · `MioloCitacao` · `MioloBarras` · `MioloProva` · `Numeral` · `CarrosselPausa` · `CarrosselRetrato` · `CarrosselMarca`.
- **Fechamento (4):** `CarrosselCTA` (Eco) · `FechamentoCentro` · `FechamentoEspelho` · `FechamentoEnvio`.
- **Feed e Stories:** `Estatico` · `Story` · `StoryInterativo` · `CapaDestaque` · `GradePerfil`.
- **Reels:** `CapaReels` · `ReelsTexto`.
- **Fundamentos:** `Manchete` · `Rotulo` · `CTA` · `Ornamentos` · `Arraste` · `SeloSerie` · `Retrato` · `ZonasSeguras`.

**Classes, de relance** (todas em `components/bundle.css`):

| Para | Classe |
| --- | --- |
| A peça | `ie-arte` + `ie-34`, `ie-story`, `ie-reels`, `ie-capa-reels`, `ie-quadrado`; textura `ie-grao`, luz `ie-brilho` ou `ie-brilho-centro` |
| A área útil | `ie-area` + `ie-entre`, `ie-base`, `ie-centro`; centralizar `ie-centrado`; largura de leitura `ie-largura` |
| Texto | estilo do `tokens.json` (`capa`, `manchete`…) + `ie-serif` ou `ie-sans`; cor `ie-suave`, `ie-ouro`, `ie-apagado`; `ie-maiusc` |
| Ornamento | `ie-rotulo`, `ie-filete`, `ie-ouro-linha`, `ie-diagonal`, `ie-metal`, `metal-text`, `ie-arraste`, `ie-costura`, `ie-selo` |
| Conteúdo | `ie-lista`, `ie-checklist`, `ie-grade` + `ie-cartao`, `ie-contraste`, `ie-conversa` + `ie-balao`, `ie-aspas`, `ie-barras`, `ie-numeral-md`, `ie-numeral-xl`, `ie-gigante` |
| Ação | `ie-chave`, `ie-botao` |
| Foto e vídeo | `ie-retrato` (+ `ie-funde-esq`), `ie-placa`, `ie-legenda`, `ie-logo` + `ie-logo-sm`/`md`/`lg` |
| Só para montar | `ie-guia`, `ie-guia-lado`, `ie-guia-grade`, `ie-guia-grade-y`, `ie-guia-sticker`, `ie-retrato-vazio`, `ie-video-vazio`, `ie-painel` |

## Variação: a identidade se repete, a composição não

A cor, as fontes, a diagonal e o chanfro são fixos. O que muda de um post para outro, e de um slide para outro, é a composição. Escolha a composição pelo que a frase pede, nunca pelo hábito.

**Capas (7).** Escolha pela frase: uma palavra que intriga pede C2; um número no título, C3; pergunta e resposta, C4; afirmação curta e forte, C5; o post mais importante da semana, C6; opinião ou história do Arthur, C7; o resto, C1.
- Nunca a mesma capa em dois posts seguidos. C7 no máximo uma a cada quatro capas.
- Em cada linha de três da grade (contando capas de Reels), pelo menos uma capa clara (C4 ou C6). É isso que impede a grade de virar um bloco preto, ainda mais no modo escuro. Confira com `GradePerfil`.

**Miolo (14).**
- Nunca a mesma composição em dois slides seguidos.
- Lista vertical (`CarrosselLista`): no máximo uma por carrossel, e nunca junto com `MioloChecklist`. Quatro itens sem ordem viram `MioloGrade`.
- Dado (`Numeral`, `MioloBarras`, `MioloProva`): no máximo dois slides de dado por carrossel, nunca seguidos, sempre com fonte.
- Slide marfim (`CarrosselPausa`): só em carrossel alternado, e nunca quando a capa já é clara. Fora o padrão "três linhas empilhadas", a pausa pode ser uma frase só.
- Pelo menos uma composição que não apareceu no carrossel anterior.

**Fechamento (4).** `CarrosselCTA` (Eco) · `FechamentoCentro` · `FechamentoEspelho` · `FechamentoEnvio`. Não repita o mesmo fechamento em dois posts seguidos. O fechamento segue o objetivo (abaixo).

**Rótulo.** Opcional. No máximo em metade dos slides do miolo. Declaração, pausa, citação e número nunca levam rótulo.

**Âncora.** Alterne onde o texto mora: topo, centro, base. Três slides seguidos com o texto no mesmo lugar é repetição.

**Ênfase.** O itálico dourado não precisa fechar a frase. Coloque-o na palavra que carrega a ideia, no começo ou no meio ("*Nada* disso aparece nos números."). Slide com numeral metálico não leva itálico dourado.

**Receitas de ritmo** (pontos de partida, não regras):
- Educativo: C2 > Declaração (costura) > Contraste > Grade > Citação > Eco.
- Dado: C3 > Numeral > Texto > Barras > Declaração > Centro.
- Objeção: C4 > Texto > Lista > Pausa > Retrato > Espelho.
- Checklist: C5 > Checklist > Texto > Declaração > Envio.
- Opinião: C7 > Declaração (costura) > Conversa > Contraste > Pausa > Envio.
- Prova: C1 > Texto > Prova > Citação do cliente > Eco.

## Objetivo e ação

Cada post tem um objetivo e uma ação só. A ação da arte e a da legenda são a mesma.

| Objetivo | Para quê | Fechamento | Ação |
| --- | --- | --- | --- |
| Alcance | chegar a quem não segue | `FechamentoEnvio` | "Envie para…" |
| Valor | virar referência, ser salvo | `FechamentoCentro` ou `FechamentoEspelho` | "Salve para…" |
| Conversa | abrir DM, gerar diagnóstico | `CarrosselCTA` (Eco) | "Comente *Palavra*" |

- O Instagram diz que pesam mais: tempo de visualização, curtidas por alcance e envios por alcance. Envio pesa mais para quem não segue; curtida, para quem já segue. Por isso, pelo menos um post em cada três pede envio.
- A palavra-chave de comentário é sempre a mesma enquanto a oferta for a mesma (hoje, *Diagnóstico*), para a resposta automática funcionar.

## Legenda, texto alternativo e hashtags

Regras curtas (o modelo completo está em `Legenda.md`):
- A primeira linha repete o gancho com a palavra que alguém digitaria na busca. Cerca de 125 caracteres aparecem antes do "mais": o gancho cabe ali.
- Até 5 hashtags, específicas do assunto e do público. É o limite do Instagram desde dezembro de 2025.
- Texto alternativo em todo post: o texto de cada slide, na ordem, e o que a imagem mostra.

## Acessibilidade

- Contraste verificado nos dois temas: todo texto passa de 4.5:1 sobre o fundo que o token indica (veja a nota de cada cor em `tokens.json`). Filete e diagonal são decorativos e nunca carregam informação sozinhos.
- Nenhuma informação só pela cor: o lado aceso do contraste também tem rótulo; a barra em foco também tem nome e valor.
- Vídeo sempre legendado. Post sempre com texto alternativo.

## Logo

- Arquivo em Logos: `impulse-logo-dourada.jpg`, dourado metálico sobre preto, sem transparência.
- Só sobre `preto-impulse`. Nunca sobre marfim ou foto. Nunca redesenhe, recolora, recorte ou distorça.
- Sempre com a classe `ie-logo`: o arquivo tem fundo preto puro, e o modo lighten faz esse preto sumir sobre o brilho e o grão.
- Tamanhos: `ie-logo-sm` (140px) como assinatura, `ie-logo-md` (200px) no story, `ie-logo-lg` (460px) só na revelação de `CarrosselMarca`.
- Aparece no estático, no story, no avatar do perfil e no carrossel de apresentação da marca. Nunca em carrossel de conteúdo nem em capa de Reels.
- Avatar do perfil: o monograma sozinho lê melhor no círculo pequeno. Peça essa versão ao designer da marca; não recorte o JPG.

## Checklist antes de publicar

- [ ] Briefing com objetivo, formato, pilar, gancho e ação; roteiro aprovado.
- [ ] Capa diferente da do post anterior; linha da grade com uma capa clara (C4 ou C6).
- [ ] Nenhuma composição repetida em slides seguidos; âncora variando; no máximo uma lista e uma pausa.
- [ ] Até 40 palavras por slide; uma ênfase por slide; nenhum travessão; nenhuma caixa alta na serifa.
- [ ] Todo número com fonte e período; nenhum dado inventado; prova com permissão do cliente.
- [ ] Nada importante a menos de 34px da borda lateral (grade) nem nas zonas da interface (story, Reels).
- [ ] Texto que precisa ser lido em `corpo` ou maior; cartões com filete; texto sobre vídeo com placa.
- [ ] `ie-arraste` na capa; costura no slide 2 quando couber.
- [ ] Uma ação só, igual na arte e na legenda.
- [ ] Guias vermelhas (`ie-guia…`) e placeholders (`ie-retrato-vazio`, `ie-video-vazio`, `00`, colchetes) removidos.
- [ ] Legenda com gancho na primeira linha, até 5 hashtags, texto alternativo escrito.
- [ ] Registro na nota de título do canvas atualizado.

## Proibido

- Travessão, caixa alta na serifa, mais de uma ênfase por slide, dourado em parágrafo, mais de um slide marfim, logo em carrossel de conteúdo, número inventado.
- A mesma capa em dois posts seguidos, a mesma composição em dois slides seguidos, mais de uma lista vertical por carrossel.
- Texto sobre vídeo sem placa, sticker desenhado na arte, repost sem transformação, print real de conversa com nome ou número.
