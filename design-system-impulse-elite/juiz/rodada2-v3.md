# Impulse Elite v3: avaliação independente (rodada 2)

**Nota final: 7.8/10** (a v2 teve 7.0)

Os pesos são os mesmos da rodada 1: Operabilidade por IA 20% · Identidade visual 15% · Consistência interna 13% · Cobertura 12% · Precisão técnica 12% · Estratégia 12% · Acessibilidade 8% · Conformidade com o formato 8%.

O que eu verifiquei:
- `compile_tokens.py` na v3: nenhum erro de gramática, 24 pares de contraste OK, e o `tokens.css` dos renders bate com o compilado.
- Comparei a v3 com a cópia da v2 que guardei em `juiz/teste/`.
- Rodei 8 testes de estresse numa cópia em `juiz/r2/teste/`, renderizados em `juiz/r2/out/` (as pranchas são `s1.png` e `s2.png`). Não toquei em `ds/`.

## 1. Os 18 pontos da rodada 1

| # | Ponto | Status | O que achei no arquivo |
|---|---|---|---|
| 1 | Fechamento x objetivo | **Resolvido** | `FechamentoCentro/preview.html:9` mostra "Salve para conferir". Os 4 READMEs de fechamento têm a linha "Objetivo · Ação". README.md:185-187 aceita o Espelho em qualquer objetivo. |
| 2 | Receitas | **Parcial** | Agora têm 7 ou 8 slides, terminam no "[fechamento]" e não há Pausa com C4 (README.md:170-177). Mas a receita Apresentação fixa "Eco com logo" e quebra a regra de âncora (ver novos, N3). |
| 3 | Grade operável | **Resolvido**, com 2 lacunas novas | A janela de três e a ordem de decisão estão em README.md:147-151, e há capa clara de Reels (`CapaReelsDividida`). As lacunas estão em N2. |
| 4 | Histórico | **Resolvido**, com lacuna nova | Há um registro único com pilar e miolo (README.md:22-34) e um fallback. Mas o briefing não pede o histórico (N1). |
| 5 | Tamanhos mínimos | **Resolvido** | `tamanho-acao` 34px, `tamanho-hora` e `tamanho-selo` 24px, `rotulo-forte` 28px em `MioloContraste` e `MioloProva`, e README.md:75 reescrito. |
| 6 | Corte do Reels na grade | **Resolvido** | bundle.css:641 tem exatamente a regra proposta. `render/v3/GradePerfil.png` mostra duas capas de Reels cortadas pelo centro. |
| 7 | Capa de destaque | **Resolvido** | `.ie-quadrado > .ie-destaque` com `cqw` e uma artboard de 1080 na prévia. No render, a letra fica com cerca de 44% do diâmetro. |
| 8 | Limites da lista | **Resolvido** | Limites novos em CarrosselLista/README.md:4 e a classe `ie-compacta`. Os testes R2Lista4, R2Lista5 e R2Lista5b (5 itens com 2 linhas) cabem na arte. |
| 9 | Tamanhos nos tokens | **Resolvido** | Estilo `capa-media`, família `tamanho` lida pelo bundle.css e nenhum `font-size` inline nas prévias. Restam literais menores, como a altura das aspas (150px) e os paddings. |
| 10 | Marfim duplicado / "alternado" | **Resolvido** | README.md:63 lista três lugares para o marfim. A Pausa tem 3 condições verificáveis (README.md:159). "Alternado" sumiu de todos os arquivos. |
| 11 | Botões desenhados | **Parcial** | O Story foi refeito, o CTA README restringe `ie-botao` e o estático não leva ação desenhada. Mas `CTA/preview.html:8` ainda mostra `ie-botao` "Ver o carrossel", e `assets/Logos/README.md:3` ainda manda logo no story. |
| 12 | Quando falta algo | **Resolvido**, com efeito colateral | A tabela está em README.md:36-46, o briefing ganhou "Material disponível" e os componentes têm "Sem foto/dado". Mas os fallbacks quebram receitas (N4). |
| 13 | Texto grande 66px e alt text | **Resolvido** | tokens.json (`ouro-escuro`), README.md:74 e :201, Legenda.md:39-41. |
| 14 | Medição e DM | **Resolvido**, com ressalvas | Linha-editorial.md:35-46 e Legenda.md:53-63. Ressalvas: uma métrica provavelmente não existe no Insights e há uma contradição de pilar (N8, N9). |
| 15 | Mais formatos | **Parcial** | Ganhou estático C1 a C7, `StoryAbertura`, Story de post compartilhado, `AnuncioVertical`, zonas de anúncio e perfil (bio, avatar, destaques). Não há `AnuncioFeed`, e o 4:5 de anúncio fica sem regra (N10). |
| 16 | Vídeo e movimento | **Resolvido** | README.md:114 e ReelsTexto/README.md: entregáveis, 1,2 a 2,5 s por bloco, corte seco, legenda automática desligada. A prévia, porém, não aplica `ie-transparente` (N7). |
| 17 | Consistência miúda (9 subitens) | **Parcial (8 de 9)** | Resolvidos: esfriou, `lead`, número sem fonte, diagonal da C6, rótulo da prova, selo, âncoras do Briefing e 28 palavras. Resta o `usage` de `brilho` em tokens.json:386, que ainda diz "Nunca em slides internos". |
| 18 | Conformidade | **Parcial** | Saíram as notas de versão, o Cover está em `tinta` e a tabela de classes está completa. O passo 5 ficou condicional (aceitável). `project/design-system.json` continua no lugar (não verificável daqui). |

Saldo: 11 resolvidos (4 deles com lacuna nova ou ressalva) e 6 parciais. O item 18 é o único com uma parte que continua não resolvida, porque não consigo verificá-la daqui.

## 2. Problemas novos ou não vistos antes (verificados)

- **N1. O histórico depende de algo frágil e o fallback mata a variação.**
  - O passo 3 (README.md:16) exige ler o registro nas notas de outros canvases, mas o briefing (Briefing.md:7-17) não tem um campo de histórico.
  - Sem resposta, a regra é "use capa clara" (README.md:34, 45). Repetida post após post, a rotação vira C4 e C6 alternadas e as outras 5 capas nunca aparecem.
- **N2. A janela de três tem becos sem saída.**
  - Reels com título afirmativo: README.md:148 manda "o resto para C6", que não é capa de Reels. `CapaReelsDividida` exige pergunta e resposta (README.md:4 do componente).
  - Estático com título afirmativo: Estatico/README.md permite C6 "trocando o arraste pela linha do @ e da logo". Mas a logo sobre marfim é proibida (README.md:208; CapaMarfim/README.md). No render `R2EstaticoC6.png`, o modo lighten faz a logo sumir no marfim.
- **N3. A âncora não é declarada por composição e uma receita quebra a regra.** Pelas classes das prévias, a receita Apresentação (README.md:177) tem três slides seguidos com o bloco de texto na base: Texto (`ie-entre`, bloco embaixo), Marca (`ie-entre`, texto embaixo) e Retrato (`ie-base`). Isso viola README.md:166. Na receita Dado, "Texto > Barras > Conversa" corre o mesmo risco: depende de `ie-entre` contar como base, e o sistema não diz.
- **N4. Os fallbacks quebram as receitas.**
  - Objeção sem foto: o Retrato vira `MioloCitacao`, e a sequência fica Contraste > Citação > Declaração, três centros seguidos. Com fechamento Centro (Valor), são quatro.
  - Opinião sem foto: C7 vira C5 ou C4. Com C5, a costura do slide 2 fica proibida (README.md:106). Com C4, a Pausa fica proibida (README.md:159).
  - Prova sem permissão: a receita perde dois slides e não há substituto.
- **N5. O README de assets contradiz o README principal.** `assets/Logos/README.md:3` diz "`ie-logo-sm` no estático… Story: `ie-logo-md`". O README.md:210-211 diz `md` no estático e "nunca em story".
- **N6. A prévia do CTA demonstra um uso proibido.** `CTA/preview.html:8` mostra `ie-botao` "Ver o carrossel", uma ação do Instagram. O README do mesmo componente proíbe `ie-botao` no Instagram. Como o passo 1 manda copiar a prévia, o erro se propaga.
- **N7. A camada do Reels sai opaca se a prévia for copiada.**
  - `ReelsTexto/preview.html:6` usa `ie-arte ie-reels`, sem `ie-transparente`. Copiada como está, a camada exporta fundo preto e cobre o vídeo. O `<body>` das prévias também pinta `var(--fundo)`.
  - O README não diz como garantir PNG com canal alfa no canvas.
  - Um Reels de 30 s gera de 15 a 25 PNGs de legenda, cada um com tempo de entrada e saída, para encaixar à mão no editor.
- **N8. A regra de pilar se contradiz.** Linha-editorial.md:19 diz que "o de conversa vem depois de um de valor sobre o mesmo pilar". A linha 20 diz que "dois posts seguidos no mesmo pilar só quando são da mesma série".
- **N9. Uma métrica provavelmente não existe.** Linha-editorial.md:42 usa "tempo médio no carrossel". Pelo que conheço, o Insights mostra tempo de visualização para Reels e não para carrossel (confira no app). O texto também não diz quando anotar o resultado no registro.
- **N10. O anúncio 4:5 de feed fica sem regra.** Briefing.md:45 diz "numa composição 4:5 (feed)". Se for uma capa, ela leva "Arraste" num anúncio de imagem única. Se for o Estático, ele leva logo, e README.md:211 proíbe logo em anúncio.
- **N11. A capa de Reels fica fraca na grade.** O título de `CapaReels` é `manchete` (120px), enquanto as capas de carrossel usam `capa` (176px). Em `render/v3/GradePerfil.png` (canto inferior direito), o título fica com cerca de 2/3 do tamanho dos vizinhos, sobre um quadro quase vazio.
- **N12. Faltam exceções e há usos desatualizados.**
  - O Estatico/README.md não desenha ação ("a ação, se houver, vai na legenda"), mas README.md:181 e :224 exigem a mesma ação na arte e na legenda, sem abrir exceção.
  - O "horário" é "a prova" (MioloConversa/README.md:1; `tamanho-hora`), mas README.md:75 o põe na lista do que "pode passar sem leitura".
  - Usos desatualizados: em tokens.json:190, `capa` cita o story (que agora usa `titulo`); em tokens.json:386, `brilho` diz "Nunca em slides internos"; o tema ainda se chama "Marfim (pausa)".
  - Briefing.md:43 e Legenda.md:47 só citam `CapaReels`.
  - CarrosselPausa/README.md não traz as 3 condições da Pausa.
  - A variante de link do Story deixa um vão de 640 × 800 para um sticker de cerca de 400 × 100.

O que passou nos testes de estresse:
- A capa de Reels dividida com pergunta em 2 linhas e resposta de 3 linhas em `manchete` termina em y≈1410, abaixo de 1480 (R2ReelsDivLonga).
- A resposta em `capa` com 3 linhas passaria de 1480, mas o README limita a 2 linhas, então o limite está certo (R2ReelsDivCapa3).
- O anúncio vertical com manchete de 3 linhas e lead de 3 linhas termina em y≈1185, abaixo de 1248 (R2Anuncio4).
- O Contraste com os textos do exemplo do Briefing cabe (R2Contraste).

## Notas por critério

| # | Critério | v2 | v3 | Em uma linha |
|---|---|---|---|---|
| 1 | Cobertura de formatos | 7.0 | 7.9 | Ganhou story de abertura e de post compartilhado, anúncio vertical, capa clara de Reels, estático C1 a C7 e perfil. Faltam anúncio 4:5, Reels clara afirmativa e fotografia real. |
| 2 | Precisão técnica 2026 | 7.0 | 8.0 | Grade com Reels, destaque, zonas Meta (270/672/65) e 66px corrigidos. Restam a exportação transparente sem verificação e uma métrica que talvez não exista. |
| 3 | Operabilidade por IA | 6.5 | 7.4 | Ordem de decisão, registro, fallback e "Objetivo · Ação" fazem grande diferença. Faltam histórico no briefing, âncora por componente, receitas que resistam ao fallback e saída para a janela forçada. |
| 4 | Identidade visual | 7.7 | 7.8 | `CapaReelsDividida` e o destaque exportado são boas adições. O miolo continua monótono e a capa de Reels escura fica pequena na grade. |
| 5 | Acessibilidade | 7.0 | 8.0 | Ação a 34px, rótulo informativo a 28px, conta de 66px e alt text sem ruído. Resta o horário-prova a 24px. |
| 6 | Estratégia | 7.5 | 8.0 | Medição por objetivo, DM pronta, bio e destaques. Restam a contradição de pilar, a métrica duvidosa e a falta de ganchos para vídeo. |
| 7 | Consistência interna | 5.8 | 7.0 | De mais de 15 contradições para cerca de 10, quase todas pequenas. As piores: README de assets, prévia do CTA e prévia do ReelsTexto. |
| 8 | Conformidade com o formato | 8.2 | 8.7 | Uma fonte por valor (família `tamanho`), `usage` limpos, Cover em ink, tabela de classes completa. Resta `design-system.json` dentro de `project/`. |

Conta: 7.9×0.12 + 8.0×0.12 + 7.4×0.20 + 7.8×0.15 + 8.0×0.08 + 8.0×0.12 + 7.0×0.13 + 8.7×0.08 = **7.76, arredondado para 7.8**.

## Maiores forças

1. **A capa é escolhida por uma ordem determinística.** São quatro regras em ordem de precedência, com janela deslizante (README.md:147-151). É o tipo de regra que uma IA segue sem ambiguidade.
2. **"Quando falta algo" é uma tabela com "Faça" e "Nunca"** (README.md:36-46), e os componentes repetem o caso: C7, `CarrosselRetrato` e `MioloProva` têm a linha "Sem foto/dado".
3. **O registro é único entre formatos.** Tem NN contínuo, pilar e lista do miolo, então as regras "composição nova", "Pausa" e "não repetir" ficam verificáveis.
4. **Os valores têm uma fonte só.** A família `tamanho` é lida pelo bundle.css, com `capa-media` e `rotulo-forte`. O contraste continua OK nos dois temas, e a regra de texto grande foi corrigida para 66px na arte.
5. **A mecânica real do Instagram está respeitada.** Post compartilhado no story (clicável), zonas de anúncio da Meta, nenhum botão desenhado, camada de Reels com tempos e legenda automática desligada, grade com corte de Reels correto.
6. **A estratégia fecha o ciclo.** Cada objetivo tem métrica principal e de apoio, há revisão a cada 9 posts, a DM da palavra-chave está pronta e há regras de bio, avatar e destaques.

## Gargalos (o que ainda trava o uso sem ajuda)

1. **O histórico não chega ao agente** (N1). Sem campo no briefing e sem garantia de ler outros canvases, o fallback "capa clara" vira a regra e a rotação de 7 capas encolhe para 2.
2. **A janela forçada não tem saída para Reels nem para estático afirmativos** (N2). O agente fica entre quebrar a janela e pôr a logo sobre marfim, ou entre quebrar a janela e reescrever o título.
3. **As receitas não são robustas.** A Apresentação viola a âncora, e os fallbacks de foto e permissão quebram Objeção, Opinião e Prova (N3, N4). Sem âncora declarada por componente, o agente não consegue checar.
4. **Prévias que contradizem o próprio README** (N6, N7). Como o passo 1 manda copiar a prévia, a camada do Reels sai opaca e o "Ver o carrossel" desenhado volta.

## Pontos fracos

1. **O miolo não mudou visualmente.** Continua preto, serifa e itálico dourado, e a fotografia segue só como placeholder. Num perfil com 20 posts, o miolo tende a parecer igual.
2. **A capa de Reels escura é a peça mais fraca da grade:** título a 120px e quadro vazio (N11).
3. **Ganchos.md não mudou e só trata a capa estática.** Não há tipos de gancho falado nem estrutura de retenção para Reels (o que dizer de 0 a 2 s, de 2 a 5 s e onde fica a virada).
4. **O fluxo do Reels é pesado e sem verificação:** um PNG por bloco de legenda e exportação com alfa não comprovada (N7).
5. **O anúncio 4:5 fica sem componente nem regra** (N10).
6. **Ainda há contradições de documentação** em assets/Logos, CTA, `brilho`, `capa`, horário e estático sem ação (N5, N6, N12).
7. **Há uma contradição de pilar na Linha-editorial** e uma métrica de apoio que provavelmente não existe (N8, N9).
8. **A variante de link do Story não tem composição própria** (N12).

## Pontos de melhoria priorizados (novos)

1. **P1: pôr o histórico no briefing.**
   - **Onde:** Briefing.md:7-17; README.md:16, 34, 45.
   - **Problema:** o histórico não está no briefing, e o fallback "capa clara" vira a regra.
   - **Mudança:**
     - Acrescentar ao briefing a linha `| Histórico | Cole as três últimas linhas do registro | Carrossel · 16 · … / Reels · 17 · … |`.
     - Trocar o fallback por: "Sem registro, pergunte só a capa da última publicação. Se ela foi clara, siga a ordem normal sem a janela. Use capa clara só quando não souber nem a última."
     - Recomendar um arquivo único de registro mantido pelo usuário (um documento de texto ou planilha colado no briefing) no lugar das notas de canvas.

2. **P1: dar saída à janela forçada para Reels e estático.**
   - **Onde:** README.md:148; CapaReelsDividida/README.md:3-4; Estatico/README.md "Outras formas".
   - **Problema:** um Reels afirmativo não tem capa clara, e um estático em C6 põe a logo sobre marfim (render R2EstaticoC6).
   - **Mudança:**
     - Criar `CapaReelsMarfim`: `ie-arte ie-capa-reels` com `data-theme="marfim"`, título em `capa` entre y 336 e 1480, sem grão e sem brilho.
     - Em README.md:148: "o resto vai para C6 (carrossel ou estático) ou `CapaReelsMarfim` (Reels)".
     - No Estatico/README.md: "Na forma C6 não há logo: a assinatura é o @ em `nota` mais 'Impulse Performance' em `rotulo`".

3. **P1: declarar a âncora de cada composição e corrigir a Apresentação.**
   - **Onde:** README.md:166, 177; README de cada miolo e fechamento.
   - **Mudança:**
     - Acrescentar a cada README uma linha "Âncora: topo | centro | base" e uma tabela no README:
       - Base: Texto, Grade, Conversa, Barras, Retrato, Marca, Envio, Eco.
       - Centro: Declaração, Checklist, Contraste, Citação, Prova, Numeral, Pausa, Centro.
       - Topo: Lista (cheia).
       - Espelho: a âncora da capa.
     - Corrigir a receita: "Apresentação: C1 com logo > Declaração > Marca > Lista > Retrato > Citação > [fechamento; em Conversa, Eco com logo]".
     - Revisar a receita Dado (Texto > Barras > Conversa).

4. **P1: dizer o que muda na receita quando falta algo.**
   - **Onde:** README.md:36-46 (acrescentar a coluna "Na receita").
   - **Mudança:**
     - Objeção sem foto: Retrato vira Grade ou Texto ancorado no topo, nunca Citação entre dois centros.
     - Opinião sem foto: C5 e sem costura, ou C4 e sem Pausa, com a Pausa trocada por Texto.
     - Prova sem permissão: use a receita Dado com dado público e fonte, ou a Educativo.

5. **P2: alinhar o README da logo.**
   - **Onde:** assets/Logos/README.md:3; README.md:210.
   - **Problema:** o README de assets manda `sm` no estático e `md` no story; o README principal diz `md` no estático e nunca no story.
   - **Mudança:** reescrever assim: "`ie-logo-md` (200px) no estático; `ie-logo-sm` (140px) na C1 e no Eco do carrossel de apresentação; `ie-logo-lg` só em CarrosselMarca. Nunca em story, capa de Reels, anúncio ou sobre marfim." Incluir a C1 em README.md:210.

6. **P2: corrigir as prévias do CTA e do ReelsTexto.**
   - **Onde:** CTA/preview.html:8; ReelsTexto/preview.html:6.
   - **Mudança:**
     - No CTA, trocar o `ie-botao` "Ver o carrossel" por três `ie-chave` (Comente, Salve, Envie). Se for manter o `ie-botao`, pô-lo num painel rotulado "Fora do Instagram" com "Agendar diagnóstico".
     - No ReelsTexto, usar `ie-arte ie-reels ie-transparente` e deixar o `ie-video-vazio` fora da artboard exportável. Acrescentar no README: "abra o PNG e confira o canal alfa antes de mandar".

7. **P2: oferecer uma alternativa às legendas em PNG.**
   - **Onde:** ReelsTexto/README.md; README.md:114.
   - **Problema:** um Reels de 30 s gera de 15 a 25 PNGs para encaixar à mão.
   - **Mudança:** "Alternativa recomendada: legenda automática do editor (Edits ou CapCut) com o preset do sistema: Montserrat 600, 44px, `marfim`, fundo preto a 78% com chanfro desligado e a mesma zona livre. Os PNGs ficam para o gancho e para editores sem preset."

8. **P2: desfazer a contradição de pilar e trocar a métrica.**
   - **Onde:** Linha-editorial.md:19-20, 42-46.
   - **Mudança:**
     - "O de conversa vem até duas publicações depois de um de valor do mesmo pilar, com outro pilar entre eles. Se vierem colados, são da mesma série."
     - Trocar "tempo médio no carrossel" por "(salvamentos + envios) ÷ alcance no carrossel; tempo médio de visualização só no Reels" (confirmar no app).
     - Acrescentar "anote as métricas 7 dias depois de publicar".

9. **P2: definir o anúncio de feed.**
   - **Onde:** Briefing.md:45; README.md:88, 211.
   - **Problema:** não há regra para o anúncio 4:5; uma capa leva "Arraste" e o estático leva logo.
   - **Mudança:** "Anúncio 4:5 = qualquer capa C1 a C6 sem `ie-arraste`, sem logo e sem @. A frase segue `capa` ou `capa-media`, e a condição da oferta vai em `lead`." Ou um componente `AnuncioFeed` com essa estrutura.

10. **P2: fortalecer a capa de Reels escura na grade.**
    - **Onde:** CapaReels/README.md:4 e preview.html.
    - **Mudança:** título em `capa` (até 3 linhas) ou `capa-media`, centrado no terço do meio do recorte 3:4 (y 600 a 1300), com o `lead` opcional. Assim o peso fica igual ao das capas de carrossel na grade.

11. **P2: criar ganchos para Reels.**
    - **Onde:** Ganchos.md (seção nova).
    - **Mudança:** tabela de gancho falado e texto na tela por tipo (perda, reenquadre, objeção, pergunta), com a estrutura de 30 s: 0 a 2 s gancho, 2 a 6 s promessa, meio com uma prova ou exemplo, últimos 3 s a ação do objetivo. O texto na tela e a fala dizem a mesma ideia com palavras diferentes.

12. **P3: abrir exceções e atualizar os usos.**
    - No README.md:181 e no checklist :224: "No estático e no Reels, a ação vive só na legenda".
    - Tirar "horário" da lista de `nota` em README.md:75, ou subir `tamanho-hora` para 28px.
    - tokens.json: `capa` (190) passa a dizer "Capas e estático"; `brilho` (386) segue README.md:104; renomear o tema para "Marfim".
    - Briefing.md:43 e Legenda.md:47: "`CapaReels` ou `CapaReelsDividida`".
    - CarrosselPausa/README.md: copiar as 3 condições de README.md:159.

13. **P3: completar o Story.**
    - **Onde:** Story/README.md:5-6.
    - **Mudança:**
      - Descrever o passo a passo no app para pôr o PNG do sistema atrás do cartão do post. O compartilhamento cria um fundo automático e o README não diz como trocá-lo. Se não houver um jeito confiável, use a alternativa: "publique o PNG como story e adicione o sticker de link para o post".
      - Para link externo, criar a guia de sticker de 560 × 140 e subir o `titulo` para `manchete`, em vez de reaproveitar o vão de 640 × 800.

14. **P3: conferir o `design-system.json` (carregado da rodada 1).** Confirmar se `project/design-system.json` deve ficar dentro de `project/`: format.md:17 lista esse nome entre os caminhos reservados.

---
Arquivos:
- Relatório: /tmp/claude-0/-home-user-estudo-hospedagem-experiencia/144ae306-6326-5779-a98a-0bb7aaedd2b2/scratchpad/juiz/rodada2.md
- Testes de estresse: /tmp/claude-0/-home-user-estudo-hospedagem-experiencia/144ae306-6326-5779-a98a-0bb7aaedd2b2/scratchpad/juiz/r2/out/ (R2*.png, mais as pranchas s1.png e s2.png)
- Cópia de teste (ds/ intocado): /tmp/claude-0/-home-user-estudo-hospedagem-experiencia/144ae306-6326-5779-a98a-0bb7aaedd2b2/scratchpad/juiz/r2/teste/project/
