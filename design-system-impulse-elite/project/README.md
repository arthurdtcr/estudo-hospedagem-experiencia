Impulse Elite é a evolução do sistema preto e dourado da Impulse Performance para o Instagram: carrossel, estático, story, Reels, anúncio e destaques. A paleta oficial continua a mesma. Muda a postura: menos cartaz, mais editorial. Serifa no lugar da condensada, ouro usado como assinatura e não como enfeite, muito espaço vazio.

## Essência

- **Silêncio antes de brilho.** O preto domina. O dourado aparece pouco e sempre no lugar que importa.
- **Uma ideia por arte.** Um gancho, uma ênfase, uma ação.
- **Ângulo do monograma.** O traço diagonal e o canto cortado da logo viram a forma da marca: `ie-diagonal` e o chanfro (`chanfro-sm`, `chanfro-lg`). Nada é arredondado.
- **Feito para o polegar.** A arte de 1080 aparece com cerca de 36% do tamanho no celular, no meio do feed, por um segundo. Se não se entende nesse tamanho, não está pronta.

## Como montar com este sistema

Siga esta ordem sempre que for criar uma peça. Ela vale para o Claude e para qualquer pessoa da equipe.

1. **Leia** este README e `tokens.json`. Para cada componente que for usar, leia `components/<Nome>/README.md` e copie a estrutura de `components/<Nome>/preview.html`. Não invente classe: se não está em `components/bundle.css`, não existe.
2. **Briefing.** Sem objetivo, formato, pilar, gancho, ação e material disponível (fotos, dados), não comece: complete pelo modelo de `Briefing.md`. Pergunte o que faltar; o que não for respondido, assuma pela seção "Quando falta algo" e diga que assumiu.
3. **Histórico.** Use as três últimas linhas do registro (abaixo), coladas no campo Histórico do briefing ou lidas nas notas dos últimos canvases, antes de escolher capa, fechamento, pausa e pilar.
4. **Roteiro antes do desenho.** Escreva o texto slide a slide numa tabela (slide, composição, texto, por quê), com no máximo 40 palavras por slide, e mostre antes de montar.
5. **Monte** num canvas do tipo Design: instale este sistema (`tokens.json` e `components/bundle.css`). Se o sistema servir `project/tokens.css`, ligue essa folha; se não, compile as variáveis de `tokens.json` numa `tokens.css` (tema `noite` em `:root`, tema `marfim` em `[data-theme="marfim"]`, as demais famílias em `:root`, uma classe por estilo de texto). Uma artboard por slide, no tamanho de Formatos, nomeada "N · função" ("1 · Capa", "4 · Pausa").
6. **Registre** a publicação na nota de título do canvas, no formato abaixo.
7. **Revise** com o Checklist, exporte e escreva a legenda e o texto alternativo por `Legenda.md`.

### O registro

Uma linha por publicação, em todo formato. Ela vai na nota de título do canvas e num arquivo único de registro mantido pela equipe (um documento ou uma planilha), de onde se copiam as três últimas linhas para o briefing:

```
Tipo · NN · Série · Título · Pilar · Objetivo · Capa · Miolo · Fechamento · Pausa
Carrossel · 16 · Série 2 · Impulsionar não é anunciar · Anúncio sem mito · Alcance · C4 · Declaração, Contraste, Texto, Checklist, Retrato · Envio · não
Reels · 17 · Série 2 · Google ou Instagram? · Anúncio sem mito · Valor · CapaReelsDividida · - · - · -
Estático · 18 · - · O anúncio é só a porta · Depois do clique · Valor · C1 · - · - · -
```

`NN` é o número da publicação, contínuo entre formatos; é o mesmo do nome do canvas ("Carrossel 16") e do `ie-selo`.

Depois de 7 dias, acrescente as métricas do objetivo no fim da linha (`Linha-editorial.md`, Medição).

**Sem registro:** pergunte só a capa da última publicação (e, se ela foi escura, a da penúltima). Se uma das duas foi clara, siga a ordem normal da capa. Use capa clara obrigatória só quando não souber nenhuma das duas. Pausa e pilar: sem registro, não use Pausa e escolha o pilar pelo briefing. Diga no roteiro o que assumiu.

## Quando falta algo

| Falta | Faça | Na receita | Nunca |
| --- | --- | --- | --- |
| Foto real do Arthur | C7 vira C5; `CarrosselRetrato` vira `MioloPergunta` ou `MioloGrade` | Objeção: Retrato vira Pergunta. Opinião: C5 e sem costura no slide 2. Apresentação: Retrato vira Pergunta | Rosto gerado por IA, banco de imagem, foto de outra pessoa |
| Número com fonte | `Numeral`, `MioloBarras` e `MioloProva` viram `MioloContraste` ou `MioloDeclaracao` com palavras | Dado: use a receita Educativo | Número aproximado, "estudos mostram", fonte genérica |
| Permissão do cliente | Não publique prova nem citação de cliente | Prova: use Dado (com dado público e fonte) ou Educativo | Cliente "anônimo" com número real |
| Objetivo | Assuma Valor (fechamento Centro, "Salve") e diga | O último slide vira `FechamentoCentro` | Duas ações |
| Gancho | Proponha três, de tipos diferentes (`Ganchos.md`) | | Começar o desenho sem gancho aprovado |
| Histórico | Pergunte a última capa ("O registro", acima) | Sem Pausa | Supor que o post anterior foi escuro |
| Logo do monograma sozinho | Use a logo completa onde o README permite; no avatar, peça o arquivo | | Recortar o JPG |

Depois de qualquer troca, confira a âncora (abaixo): a sequência nova não pode ter três slides seguidos com a mesma âncora.

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
- `destaque` só em: rótulo, palavra em `<em>`, numeral, filete dourado, barra em foco, ação. Nunca em parágrafo.
- Tema `noite` em quase tudo. Tema `marfim` em três lugares: as capas claras (C4, C6, `CapaReelsDividida`, `CapaReelsMarfim`), o `FechamentoEspelho` de uma capa clara e a Pausa. Lá o destaque vira `bronze`.
- Degradê metálico (`metal-text`, `ie-metal`): só em numeral e filete curto. As paradas são `ouro-escuro`, `ouro-medio`, `ouro-claro`, `champagne`, `ouro-medio`, `ouro-escuro`.
- Texto de apoio sobre marfim é `cinza-grafite`, nunca `cinza-texto` (não tem contraste).
- Cartão e balão em `superficie` levam sempre `filete` em volta: grafite sobre preto é 1.2:1 e some no celular.
- Sobre vídeo, texto só em cima de `placa`, e só em `tinta` ou `destaque`.
- **Modo escuro do app.** O `preto-impulse` se funde com a interface: a arte perde a borda e vira texto flutuando. Por isso a grade alterna capas claras e o texto sempre respeita as margens.

## Tipografia

- Duas famílias, ambas do Google Fonts: `serif` (Instrument Serif, com itálico) para manchetes e números; `sans` (Montserrat, a mesma geometria da palavra IMPULSE na logo) para texto e rótulos.
- Estilos para a arte em 1080 de largura: `numeral` 280, `capa` 176, `capa-media` 150, `manchete` 120, `titulo` 84, `item` 56 na serifa; `lead` 40, `corpo` 34, `rotulo-forte` 28, `nota` 24, `rotulo` 22 na sans; no vídeo, `gancho-video` 104 (serifa) e `legenda-video` 44 (sans 600). Os tamanhos de dentro dos componentes (palavra gigante, numerais, aspas, ação, selo, horário) estão na família `tamanho` de `tokens.json`.
- **Conta do celular:** px da arte × 0,36 ≈ pt na tela. `corpo` (34px) vira cerca de 12pt; `nota` (24px), cerca de 8,6pt.
- Tudo que precisa ser lido fica em `corpo` ou maior, inclusive a ação (`tamanho-acao`, 34px). Rótulo que carrega informação (o lado de um contraste, antes e depois) vai em `rotulo-forte`. `nota` só para o que pode passar sem leitura: fonte, crédito, dica. O horário do balão é prova e vai em `tamanho-hora` (28px). `rotulo` (22px) é a única exceção abaixo de 24px e só nomeia o assunto do slide.
- Serifa sempre em caixa normal, com ponto final. Ênfase em itálico `<em>`, uma por slide.
- Montserrat só nos pesos 400, 500 e 600.

## Formatos e zonas seguras

| Peça | Tamanho | Classe | Zona livre |
| --- | --- | --- | --- |
| Carrossel, estático | 1080 × 1350 (4:5) | `ie-arte` | `margem-x` 88, `margem-y` 112; a grade corta 34px de cada lado |
| Post 3:4 (opcional) | 1080 × 1440 | `ie-arte ie-34` | igual ao 4:5; preenche a grade sem corte, mas não vira anúncio |
| Anúncio de feed | 1080 × 1350 (4:5) | `ie-arte` (`AnuncioFeed`) | como o carrossel; nunca 3:4 |
| Story | 1080 × 1920 | `ie-arte ie-story` | 250 em cima, 340 embaixo |
| Reels (texto na tela) | 1080 × 1920 | `ie-arte ie-reels ie-transparente` | 250 em cima, 440 embaixo, 140 à direita |
| Capa de Reels | 1080 × 1920 | `ie-arte ie-capa-reels` | título entre y 336 e y 1480 (a grade corta 240 em cima e embaixo) |
| Anúncio vertical | 1080 × 1920 | `ie-arte ie-anuncio` | 270 em cima, 672 embaixo, 65 dos lados |
| Capa de destaque | 1080 × 1080 | `ie-arte ie-quadrado` | o círculo ocupa a arte; o Instagram recorta o centro |

- O carrossel aceita até 20 slides; o sistema usa de 7 a 10. Todos os slides têm a proporção do primeiro.
- As medidas estão em `tokens.json` (família `formato`) e no componente `ZonasSeguras`. Elas mudam com o app: confira na prévia do Instagram antes de publicar.
- Exporte em PNG, 1080 de largura, sRGB, um arquivo por slide, nomeado `NN-slide-MM.png` (`15-slide-01.png`). Camadas de vídeo com fundo transparente.

## Grid e respiro

- Texto ancorado: capa na base, slides internos com rótulo no topo e bloco na metade de baixo, ou centro.
- Espaço entre blocos em `space-6` (48px); manchete e resto separados por `space-12` (96px) quando couber.

**Âncora de cada composição** (onde mora o bloco de texto principal; a regra de Variação usa esta tabela):

| Âncora | Composições |
| --- | --- |
| Topo | `MioloPergunta`; `CarrosselTexto` sem rótulo e ancorado em cima |
| Centro | `MioloDeclaracao`, `MioloChecklist`, `MioloContraste`, `MioloCitacao`, `MioloProva`, `Numeral`, `CarrosselPausa`, `FechamentoCentro` |
| Base | `CarrosselTexto` (com rótulo), `MioloGrade`, `MioloConversa`, `MioloBarras`, `CarrosselRetrato`, `CarrosselMarca`, `CarrosselCTA` (Eco), `FechamentoEnvio` |
| Cheia | `CarrosselLista`: ocupa a altura toda e quebra qualquer sequência |
| Da capa | `FechamentoEspelho`: a âncora da capa que ele espelha |

## Formas e textura

- `canto` é 0 em tudo. O único corte é o chanfro no canto superior direito, como o monograma: ações, cartões, balões, barras, selos, placas e fotos em moldura. O círculo da capa de destaque é imposto pelo Instagram.
- `ie-grao` (opacidade `grao`) em toda arte Noite: dá textura de papel.
- `ie-brilho` (opacidade `brilho`) só em capa, fechamento, estático, story, capa de Reels e anúncio. No miolo, só `CarrosselMarca` (`ie-brilho-centro`), porque a luz é da logo.
- `ie-diagonal`: no máximo uma por arte, entrando por uma borda, longe do texto e do `ie-arraste`.
- `ie-arraste` em toda capa de carrossel: o filete sai pela borda direita (na C5, centralizada, ele fica curto). `ie-costura` no slide 2 recebe esse filete quando a capa não é C5 e a base esquerda do slide 2 está livre.
- Sem sombra, sem cartão com borda colorida na lateral, sem ícone decorativo, sem emoji.

## Fotografia e vídeo

- Pessoas sempre em preto e branco (`ie-retrato`): `grayscale(1)`, contraste 1.12, fundo escuro, luz lateral, recorte do peito para cima.
- A base da foto se dissolve no `fundo`. Foto que sangra a borda não leva chanfro; foto em moldura leva `chanfro-lg`.
- Nunca foto colorida, banco de imagem genérico, rosto gerado por IA ou pessoa sorrindo para a câmera sem contexto.
- **Reels:** o vídeo é gravado em 1080 × 1920, vertical (confira no app a taxa de quadros aceita). O Claude não edita vídeo: entrega o roteiro com tempos, a camada PNG transparente do gancho (`ReelsTexto`) e a capa (`CapaReels`, `CapaReelsDividida` ou `CapaReelsMarfim`). A legenda da fala sai do editor (Edits ou CapCut) com o preset do sistema, descrito em `ReelsTexto`. O gancho entra no segundo 0 e sai no 2; cada bloco de legenda fica de 1,2 a 2,5 segundos; corte seco, sem animação de texto. Com a legenda queimada, desligue a legenda automática do Instagram.
- **Originalidade:** desde abril de 2026 o Instagram tira das recomendações as contas que mais repostam do que criam, também em foto e carrossel. Tudo aqui é gravado, escrito e desenhado pela Impulse; trecho de terceiro só com comentário por cima e crédito.

## Componentes

Cada componente tem uma prévia viva e um README com quando usar, o que fornecer, a estrutura e o que não fazer.

- **Capas de carrossel (7):** C1 `CarrosselCapa` (Base) · C2 `CapaPalavra` · C3 `CapaNumero` · C4 `CapaDividida` · C5 `CapaMoldura` · C6 `CapaMarfim` · C7 `CapaRosto`.
- **Miolo (15):** `CarrosselTexto` · `MioloDeclaracao` · `MioloPergunta` · `CarrosselLista` · `MioloGrade` · `MioloChecklist` · `MioloContraste` · `MioloConversa` · `MioloCitacao` · `MioloBarras` · `MioloProva` · `Numeral` · `CarrosselPausa` · `CarrosselRetrato` · `CarrosselMarca`.
- **Fechamento (4):** `CarrosselCTA` (Eco) · `FechamentoCentro` · `FechamentoEspelho` · `FechamentoEnvio`.
- **Reels:** `CapaReels` · `CapaReelsDividida` · `CapaReelsMarfim` · `ReelsTexto`.
- **Feed, Stories e anúncio:** `Estatico` · `StoryAbertura` · `StoryInterativo` · `Story` (divulgação) · `AnuncioFeed` · `AnuncioVertical` · `CapaDestaque` · `GradePerfil`.
- **Fundamentos:** `Manchete` · `Rotulo` · `CTA` · `Ornamentos` · `Arraste` · `SeloSerie` · `Retrato` · `ZonasSeguras`.

**Classes, de relance** (todas em `components/bundle.css`):

| Para | Classe |
| --- | --- |
| A peça | `ie-arte` + `ie-34`, `ie-story`, `ie-reels`, `ie-capa-reels`, `ie-anuncio`, `ie-quadrado`, `ie-transparente`; textura `ie-grao`; luz `ie-brilho` ou `ie-brilho-centro` |
| A área útil | `ie-area` + `ie-entre`, `ie-base`, `ie-centro`; centralizar `ie-centrado`; largura de leitura `ie-largura` |
| Texto | estilo do `tokens.json` (`capa`, `capa-media`, `manchete`, `rotulo-forte`…) + `ie-serif` ou `ie-sans`; cor `ie-suave`, `ie-ouro`, `ie-apagado`; `ie-maiusc` |
| Ornamento | `ie-rotulo`, `ie-filete`, `ie-ouro-linha`, `ie-diagonal`, `ie-metal`, `metal-text`, `ie-arraste`, `ie-costura`, `ie-selo` |
| Capas | `ie-gigante` (C2), `ie-numeral-xl` (C3), `ie-dividida-topo` + `ie-dividida-base` (C4, Reels), `ie-moldura` (C5) |
| Pergunta no miolo | `ie-pergunta-topo` + `ie-pergunta-base` |
| Conteúdo | `ie-lista` (+ `ie-compacta`), `ie-checklist`, `ie-grade` + `ie-cartao` + `ie-cartao-num`, `ie-contraste` + `ie-contraste-lado` + `ie-contraste-fio`, `ie-conversa` + `ie-balao` (+ `ie-eu` para o cliente) + `ie-balao-hora` (+ `ie-alerta`), `ie-aspas`, `ie-barras` + `ie-barra` (+ `ie-foco`) + `ie-barra-linha` + `ie-barra-fio` + `ie-barra-valor`, `ie-numeral-md` |
| Ação | `ie-chave` (no Instagram), `ie-botao` (só fora dele) |
| Foto e vídeo | `ie-retrato` (+ `ie-funde-esq`), `ie-placa`, `ie-legenda`, `ie-logo` + `ie-logo-sm`/`md`/`lg`, `ie-destaque` |
| Miniaturas | `ie-perfil` + `ie-perfil-tile` (grade do perfil), `ie-miniatura` (capa dentro do story) |
| Só para montar | `ie-guia`, `ie-guia-lado`, `ie-guia-grade` (+ `ie-esq`/`ie-dir`), `ie-guia-grade-y`, `ie-guia-sticker`, `ie-retrato-vazio`, `ie-video-vazio`, `ie-painel` |

## Variação: a identidade se repete, a composição não

A cor, as fontes, a diagonal e o chanfro são fixos. O que muda de um post para outro, e de um slide para outro, é a composição.

**Escolha da capa, nesta ordem** (vale para carrossel, estático e Reels; a regra de cima vence a de baixo):
1. **Janela de três:** entre esta capa e as duas publicações anteriores, pelo menos uma é clara (C4, C6, `CapaReelsDividida` ou `CapaReelsMarfim`). Se as duas anteriores foram escuras, esta é clara:
   - carrossel: pergunta e resposta vai para C4; o resto, para C6;
   - Reels: pergunta e resposta vai para `CapaReelsDividida`; o resto, para `CapaReelsMarfim`;
   - estático: C4 ou C6 sem logo (a assinatura é o @ e "Impulse Performance" em `rotulo`).
2. **Não repetir** a capa da publicação anterior.
3. **C7** no máximo uma a cada quatro capas.
4. **Pela frase:** uma palavra que intriga pede C2; um número no título, C3; pergunta e resposta, C4; afirmação curta e forte, C5; o post mais importante da semana, C6; opinião ou história do Arthur, C7; o resto, C1.

Confira o resultado com `GradePerfil`.

**Miolo (14).**
- Nunca a mesma composição em dois slides seguidos.
- Lista vertical (`CarrosselLista`): no máximo uma por carrossel, e nunca junto com `MioloChecklist`. Quatro itens sem ordem viram `MioloGrade`.
- Dado (`Numeral`, `MioloBarras`, `MioloProva`): no máximo dois slides de dado por carrossel, nunca seguidos, sempre com fonte.
- **Pausa** (`CarrosselPausa`) só quando as três condições valem: a capa é escura; a publicação anterior não teve Pausa (registro); o carrossel tem 8 slides ou mais.
- Pelo menos uma composição de miolo que não está no registro da publicação anterior.

**Fechamento (4).** `CarrosselCTA` (Eco) · `FechamentoCentro` · `FechamentoEspelho` · `FechamentoEnvio`. O fechamento segue o objetivo (abaixo). Não repita o mesmo fechamento em dois posts seguidos.

**Rótulo.** Opcional. No máximo em metade dos slides do miolo. Declaração, pausa, citação e numeral nunca levam rótulo; a prova leva "Resultado".

**Âncora.** Alterne onde o texto mora, pela tabela de âncoras em Grid e respiro. Três slides seguidos com a mesma âncora é repetição; a capa conta como base.

**Ênfase.** O itálico dourado não precisa fechar a frase. Coloque-o na palavra que carrega a ideia, no começo ou no meio ("*Nada* disso aparece nos números."). Slide com numeral metálico não leva itálico dourado.

**Receitas de ritmo.** Pontos de partida de 7 ou 8 slides; o último é sempre o fechamento do objetivo.
- Educativo: C2 > Declaração (costura) > Contraste > Texto > Pausa > Grade > Citação > [fechamento].
- Dado: C3 > Numeral > Texto > Barras > Declaração > Conversa > [fechamento].
- Objeção: C4 > Texto > Lista > Contraste > Retrato > Declaração > [fechamento].
- Checklist: C5 > Declaração > Texto > Checklist > Conversa > Citação > [fechamento].
- Opinião: C7 > Declaração (costura) > Conversa > Pausa > Contraste > Texto > Citação > [fechamento].
- Prova: C1 > Texto > Prova > Citação do cliente > Grade > Declaração > [fechamento].
- Apresentação: C1 com logo > Declaração > Marca > Lista > Retrato > Citação > [fechamento; em Conversa, Eco com logo].

As receitas já respeitam âncora, pausa, dado e costura. Ao trocar um slide (por falta de foto, dado ou permissão), refaça a conferência da âncora.

## Objetivo e ação

Cada post tem um objetivo e uma ação só. No carrossel, a ação da arte e a da legenda são a mesma. No estático e no Reels a arte não desenha ação: ela vive na legenda (e, no Reels, também na fala dos últimos segundos).

| Objetivo | Para quê | Fechamento | Ação |
| --- | --- | --- | --- |
| Alcance | chegar a quem não segue | `FechamentoEnvio` ou Espelho | "Envie para…" |
| Valor | virar referência, ser salvo | `FechamentoCentro` ou Espelho | "Salve para…" |
| Conversa | abrir DM, gerar diagnóstico | `CarrosselCTA` (Eco) ou Espelho | "Comente *Palavra*" |

- O Instagram diz que pesam mais: tempo de visualização, curtidas por alcance e envios por alcance. Envio pesa mais para quem não segue; curtida, para quem já segue. Por isso, em cada três posts, um de cada objetivo.
- A palavra-chave de comentário é sempre a mesma enquanto a oferta for a mesma (hoje, *Diagnóstico*), para a resposta automática funcionar. A mensagem dela está em `Legenda.md`; a medição, em `Linha-editorial.md`.

## Legenda, texto alternativo e hashtags

Regras curtas (o modelo completo está em `Legenda.md`):
- A primeira linha repete o gancho com a palavra que alguém digitaria na busca. Cerca de 125 caracteres aparecem antes do "mais": o gancho cabe ali.
- Até 5 hashtags, específicas do assunto e do público. É o limite do Instagram desde dezembro de 2025.
- Texto alternativo em todo post, um por slide: o texto do slide, na ordem, e o que a imagem mostra.

## Acessibilidade

- Contraste verificado nos dois temas: todo texto passa de 4.5:1 sobre o fundo que o token indica (veja a nota de cada cor em `tokens.json`). A exceção de texto grande da WCAG (3:1) só vale a partir de 66px na arte, por causa da redução no celular. Filete e diagonal são decorativos e nunca carregam informação sozinhos.
- Nenhuma informação só pela cor: o lado aceso do contraste também tem rótulo; a barra em foco também tem nome e valor.
- Vídeo sempre legendado. Post sempre com texto alternativo.

## Logo

- Arquivo em Logos: `impulse-logo-dourada.jpg`, dourado metálico sobre preto, sem transparência.
- Só sobre `preto-impulse`. Nunca sobre marfim ou foto. Nunca redesenhe, recolora, recorte ou distorça.
- Sempre com a classe `ie-logo`: o arquivo tem fundo preto puro, e o modo lighten faz esse preto sumir sobre o brilho e o grão.
- Tamanhos: `ie-logo-md` (200px) no estático; `ie-logo-sm` (140px) na capa C1 e no fechamento Eco do carrossel de apresentação; `ie-logo-lg` (460px) só na revelação de `CarrosselMarca`.
- Aparece no estático escuro, no avatar do perfil e no carrossel de apresentação da marca. Nunca em carrossel de conteúdo, story (a foto do perfil já está no topo), capa de Reels, anúncio (o nome do perfil já aparece) ou sobre marfim.
- Avatar do perfil: o monograma sozinho lê melhor no círculo pequeno. Peça essa versão ao designer da marca; não recorte o JPG.

## Checklist antes de publicar

- [ ] Briefing com objetivo, formato, pilar, gancho, ação e material; roteiro aprovado.
- [ ] Histórico no briefing (ou a última capa perguntada); capa escolhida pela ordem de decisão.
- [ ] Nenhuma composição repetida em slides seguidos; nunca três âncoras iguais seguidas (tabela de âncoras); no máximo uma lista, dois dados e uma pausa (com as três condições).
- [ ] Até 40 palavras por slide; uma ênfase por slide; nenhum travessão; nenhuma caixa alta na serifa.
- [ ] Todo número com fonte e período; nenhum dado inventado; prova com permissão do cliente.
- [ ] Nada importante a menos de 34px da borda lateral nem nas zonas da interface (story, Reels, anúncio).
- [ ] Texto que precisa ser lido em `corpo` ou maior; rótulo com informação em `rotulo-forte`; cartões com filete; texto sobre vídeo com placa.
- [ ] `ie-arraste` na capa; costura no slide 2 quando couber.
- [ ] Uma ação só, a do objetivo; no carrossel, igual na arte e na legenda; no estático e no Reels, só na legenda; nenhum botão desenhado no Instagram.
- [ ] Guias vermelhas (`ie-guia…`) e placeholders (`ie-retrato-vazio`, `ie-video-vazio`, `00`, colchetes) removidos.
- [ ] Legenda com gancho na primeira linha, até 5 hashtags, texto alternativo por slide.
- [ ] Registro escrito na nota de título do canvas e no arquivo de registro.

## Proibido

- Travessão, caixa alta na serifa, mais de uma ênfase por slide, dourado em parágrafo, marfim fora dos três lugares permitidos, logo em carrossel de conteúdo, número inventado.
- A mesma capa em duas publicações seguidas, três capas escuras seguidas, a mesma composição em dois slides seguidos, mais de uma lista vertical por carrossel.
- Texto sobre vídeo sem placa, botão ou sticker desenhado na arte, repost sem transformação, print real de conversa com nome ou número, rosto gerado por IA.
