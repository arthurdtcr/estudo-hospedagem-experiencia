# Impulse Elite: avaliação independente (rodada 1)

**Nota final: 7.0/10**

Pesos: Operabilidade por IA 20% · Identidade visual 15% · Consistência interna 13% · Cobertura 12% · Precisão técnica 12% · Estratégia 12% · Acessibilidade 8% · Conformidade com o formato 8%. O sistema existe para o Claude operar sozinho, por isso operabilidade e consistência somam 33% do peso.

O que eu verifiquei:
- `compile_tokens.py`: nenhum erro de gramática, 24 pares de contraste OK.
- Renders de estresse: montei variantes numa cópia em `juiz/teste/`, renderizei em `juiz/out_render/` (T1 a T6) e não toquei em `ds/`.
- Simulei o tamanho no celular, a 390px de largura, em `juiz/out/phone1..3.png`.

## Notas por critério

| # | Critério | Nota | Em uma linha |
|---|---|---|---|
| 1 | Cobertura de formatos e tipos de conteúdo | 7.0 | O carrossel é profundo (7 capas, 14 miolos, 4 fechamentos). O estático tem uma composição só, a capa de Reels também e o story é raso. Faltam anúncio, foto/vídeo real, abertura e repost de story. |
| 2 | Precisão técnica com o Instagram 2026 | 7.0 | Medidas corretas e com ressalvas honestas. Há bugs de implementação: a grade corta errado a capa de Reels, a capa de destaque sai com 300px, a regra de linha da grade é instável e falta a zona de topo de anúncio. |
| 3 | Operabilidade por IA | 6.5 | O fluxo é ótimo e os READMEs são uniformes. Mas há contradições entre objetivo, receitas e prévias, o histórico depende de algo sem fallback, falta precedência entre regras e não há plano para quando falta foto ou dado. |
| 4 | Identidade e qualidade visual | 7.7 | Sofisticada e coerente, com capas excelentes. O miolo é monótono (preto, serifa e itálico dourado), tem vazios grandes e textos secundários pequenos. Os placeholders de foto tomam o lugar de imagem real. |
| 5 | Acessibilidade e legibilidade | 7.0 | O contraste é exemplar nos dois temas, inclusive a placa no pior caso. Mas o próprio CSS viola os mínimos (CTA 30px, hora 22px), o rótulo carrega informação a ~8pt e a regra WCAG de texto grande foi aplicada ao pixel da arte. |
| 6 | Estratégia de conteúdo | 7.5 | Objetivo, fechamento e ação ligados aos sinais citados por Mosseri, ganchos tipificados com exemplos reais, originalidade 2026. Falta ciclo de medição, a mensagem da DM e estratégia de Reels. |
| 7 | Consistência interna | 5.8 | Mais de 15 contradições verificadas entre README, tokens, CSS, READMEs de componente e prévias, inclusive em exemplos do próprio sistema. |
| 8 | Conformidade com o formato Design System | 8.2 | Arquivos, marcadores, Cover, tokens e notas de contraste dentro do formato. Ressalvas: valores fora dos tokens, notas de versão no `usage`, compilação manual de `tokens.css`, nome do Cover em dourado. |

## Maiores forças

1. **O fluxo de trabalho é bom para um agente.** Briefing, três ganchos, roteiro em tabela, montagem, legenda e alt, registro e checklist, com a regra "pergunte o que faltar, assuma o resto e diga que assumiu" (README.md:12-20, Briefing.md:3).
2. **Os tokens são semânticos e verificados.** Há dois temas, `on-destaque` e o contraste por par anotado no `usage`, incluindo a placa sobre vídeo branco no pior caso (tokens.json:19, 10.4:1 conferido à mão). Compila sem erro.
3. **A identidade é forte e própria.** O chanfro e a diagonal do monograma viraram linguagem (`chanfro-sm`/`lg`, `ie-diagonal` a 58°). As 7 capas são genuinamente distintas (v2-capas.png) e o ouro é usado como assinatura, não como enfeite.
4. **O Instagram está tokenizado.** A família `formato` traz o corte de 34px da grade 3:4, os 240px da capa de Reels e as zonas de story e Reels, com guias de montagem (`ie-guia*`) e ressalvas ("confira no app", "não confirmado pela Meta").
5. **A estratégia está amarrada a mecanismos reais.** Objetivo leva a fechamento e ação (README.md:150-157), palavra-chave estável para a automação, 5 hashtags, busca pela primeira linha da legenda, alt text por slide e a regra de originalidade de abril de 2026.
6. **Os READMEs de componente seguem um molde único** (Use quando / Você fornece / Estrutura / Não faça), com limites quantitativos (palavras, letras, itens). É exatamente o que uma IA precisa.

## Gargalos (o que trava o uso real hoje)

1. **A ação errada sai da prévia.** A tabela manda `FechamentoCentro` e `FechamentoEspelho` para Valor ("Salve para…", README.md:153). As duas prévias mostram "Comente Diagnóstico" (FechamentoCentro/preview.html:9, FechamentoEspelho/preview.html:12) e nenhuma prévia demonstra "Salve". Como o passo 1 manda copiar a prévia, o Claude vai repetir a ação de conversa num post de valor.
2. **As receitas contradizem as regras.** A receita "Objeção" (C4 > … > Pausa, README.md:141) viola a linha 127 ("nunca quando a capa já é clara"). As 6 receitas têm 5 a 6 slides, abaixo do mínimo de 7 (README.md:64). Os fechamentos fixos não batem com o objetivo dos pilares que as recomendam (Linha-editorial.md:9-13).
3. **A regra da grade não é operável.** A grade se desloca uma posição a cada post, então "cada linha de três" muda de composição. Não há precedência entre "escolha a capa pela frase" e "uma capa clara por linha". A capa de Reels conta na grade, mas só existe escura e numa composição única.
4. **O histórico tem dependência frágil.** O README manda ler "o título dos três últimos canvases Carrossel NN" (README.md:17), sem fallback se o agente não tiver esse acesso. Reels e estáticos não são registrados, embora contem na grade. O formato do registro não tem o pilar (README.md:19), mas Linha-editorial.md:34-37 exige o pilar.
5. **Três peças exportam errado** (verificado em render):
   - A capa de destaque sai com um círculo de 300px numa arte de 1080 (T2Destaque.png).
   - `GradePerfil` mostra o topo da capa de Reels em vez do centro e esconde o `lead` (T3Grade.png).
   - `CarrosselLista` no limite documentado estoura a arte, que vai até y≈1482 de 1350 (T4Lista.png).
6. **Não há plano para entradas que faltam.** Não existe nenhuma foto real do Arthur nos assets, então C7, `CarrosselRetrato` e `Retrato` ficam inutilizáveis. Sem dado com fonte, `Numeral`, `MioloBarras` e `MioloProva` também. O README não diz o que usar no lugar.

## Pontos fracos

1. **Muitos valores ficam fora dos tokens.**
   - Os tamanhos 150 e 156px entram por `style` inline em 6 prévias.
   - O CSS tem 420, 560, 168, 360, 132, 48, 30 e 22px literais, além de paddings de 28, 52, 44 e 80px.
   - Editar a página de tokens não muda esses valores.
2. **O CSS viola os mínimos do próprio README** (README.md:48).
   - `.ie-chave > span` e `.ie-botao` têm 30px (bundle.css:170, 184), mas a ação precisa ser lida.
   - `.ie-balao-hora`, que é "a prova", e `.ie-selo > span` têm 22px (bundle.css:403, 465).
   - Os rótulos "Antes/Depois" e "O que você vê" carregam informação a 22px, cerca de 8pt no celular (phone1/phone2.png).
3. **O miolo tende à monotonia.** Quase todo slide é fundo preto, serifa e itálico dourado. `MioloProva` e `CarrosselTexto` deixam a metade de cima vazia e o bloco útil fica pequeno no celular. Não há fotografia real (só placeholders) e a logo do estático some no celular: "PERFORMANCE" fica ilegível a 140px.
4. **Fora do carrossel, os formatos são rasos.**
   - O estático tem uma só composição e a capa de Reels também.
   - O story de divulgação é uma capa esticada com um botão desenhado, que não é clicável.
   - A sequência de stories cita uma "Abertura" (Briefing.md:44) que não existe como componente.
5. **Não há especificação de vídeo nem de movimento.** Faltam duração, fps, codec, tempo por bloco de legenda, entrada e saída do gancho e o que fazer com a legenda nativa do Instagram. O Claude só produz a camada PNG e isso não está dito.
6. **Não há ciclo de medição.** Falta a métrica por objetivo no Insights, a revisão periódica e o texto da DM automática de "Diagnóstico" (Legenda.md:49 cita "a mesma mensagem de abertura" sem fornecê-la).
7. **Há termos e semânticas ambíguos.**
   - "Carrossel alternado" (README.md:127) não é definido em lugar nenhum.
   - `SeloSerie` diz "número do episódio", mas o registro usa o número global ("Série 2 · 16", canvases "Carrossel NN").
   - A classe `ie-eu` é usada para o cliente, não para quem atende.
8. **Os exemplos do sistema violam as próprias regras.**
   - O roteiro do Briefing põe os slides 5, 6 e 7 (Grade, Retrato, Envio) todos em `ie-base`, contra README.md:134.
   - `CarrosselRetrato` traz "mais de R$200 milhões" sem fonte (preview.html:14), contra README.md:27.
   - A diagonal das Ornamentos corta "MONOGRAMA".
   - A diagonal da `CapaMarfim` não cruza a borda, contra README.md:79.

## Pontos de melhoria priorizados

1. **P1: alinhar fechamento e objetivo.**
   - **Onde:** README.md:150-154; FechamentoCentro/preview.html:9 e README.md:3; FechamentoEspelho/preview.html:12.
   - **Problema (verificado):** a tabela diz Valor e "Salve", as prévias dizem "Comente Diagnóstico" e o "Use quando" do Centro descreve conversa ("já explicou a oferta").
   - **Mudança:**
     - Trocar as chaves para `<span class="ie-chave"><span>Salve <b>para conferir</b></span></span>` (Centro) e `Salve <b>para a reunião</b>` (Espelho).
     - Reescrever o "Use quando" do Centro: "Objetivo Valor: o carrossel entregou um método e o fechamento pede para salvar".
     - Acrescentar em cada README de fechamento a linha "Objetivo · Ação".

2. **P1: refazer as receitas de ritmo.**
   - **Onde:** README.md:139-144; Linha-editorial.md:9-13.
   - **Problema (verificado):** a receita Objeção põe Pausa depois de C4, contra README.md:127 e CapaDividida/README.md:6. As receitas têm 5 a 6 slides contra o mínimo de 7 (README.md:64). O fechamento fixo de cada receita não bate com o objetivo do pilar que a recomenda.
   - **Mudança:**
     - Escrever cada receita com 7 posições e o último passo como "[fechamento do objetivo]". Exemplo: "Objeção: C4 > Texto > Lista > Contraste > Retrato > Declaração > [fechamento do objetivo]".
     - Tirar a Pausa de qualquer receita com C4 ou C6.
     - Na Linha-editorial, listar receita e objetivo como pares válidos.

3. **P1: tornar a regra da grade operável.**
   - **Onde:** README.md:119-121; GradePerfil/README.md:6; Linha-editorial.md:25; CapaReels.
   - **Problema:** as "linhas de três" mudam a cada post, não há precedência entre as regras e a capa de Reels é só escura e numa composição só.
   - **Mudança:** substituir por uma janela de três: "entre esta capa e as duas publicações anteriores, de qualquer formato, pelo menos uma é clara (C4, C6 ou CapaReels Marfim)". Ordem de decisão:
     1. Janela de três.
     2. Não repetir a capa anterior.
     3. C7 no máximo uma em quatro.
     4. Mapeamento pela frase.
   - Se o passo 1 exigir capa clara: pergunta vai para C4, o resto para C6.
   - Criar `CapaReels` com `data-theme="marfim"` (sem grão e sem brilho) e uma segunda composição de capa de Reels.

4. **P1: dar ao histórico um formato único e um fallback.**
   - **Onde:** README.md:17-19, 128; Briefing.md:25; Linha-editorial.md:31-37.
   - **Mudança:**
     - Registro único para todo formato: "Tipo · NN · Série/ep · Título · Pilar · Objetivo · Capa · Miolo: [composições] · Fechamento · Pausa". Com as composições do miolo no registro, a regra da linha 128 ("uma composição nova") passa a ser verificável.
     - Fallback: "Se não conseguir ler os registros, pergunte ao usuário as três últimas capas, objetivos e pilares. Sem resposta, assuma 'desconhecido', use capa clara e diga isso no roteiro."

5. **P1: corrigir os tamanhos mínimos.**
   - **Onde:** bundle.css:170, 184, 403, 465; README.md:48, 169; tokens.json.
   - **Problema (verificado):** a ação tem 30px, a hora e o selo têm 22px, e rótulos carregam informação a 22px.
   - **Mudança:**
     - Criar o estilo `acao` em `type` (sans, 600, 34px, `0.2em`) e usá-lo em `.ie-chave > span` e `.ie-botao`.
     - Subir `.ie-balao-hora` para 24px (`nota`).
     - Para rótulos que nomeiam coluna ou estado, criar `rotulo-forte` (28px) ou exigir que a informação se repita no texto ("conversas por mês, antes").
     - Corrigir a frase "única exceção abaixo de 24px".

6. **P1: corrigir o corte da capa de Reels na grade.**
   - **Onde:** bundle.css:618; GradePerfil/preview.html.
   - **Problema (verificado, T3Grade.png):** `scale(0.32)` mais o corte lateral de 34px mostra o topo (0 a 1350) da capa de Reels, com a faixa que a grade corta, e esconde o `lead`.
   - **Mudança:** acrescentar `.ie-perfil-tile > .ie-arte.ie-capa-reels { transform: translateY(calc(-1 * var(--grade-corte-y) * 0.3)) scale(0.3); }` e incluir uma capa de Reels na prévia.

7. **P1: corrigir a exportação da capa de destaque.**
   - **Onde:** bundle.css:222-241; CapaDestaque/README.md:5 e preview.html.
   - **Problema (verificado, T2Destaque.png):** o README manda exportar 1080 × 1080, mas `.ie-destaque` é fixo em 300px; o círculo fica com 28% do diâmetro.
   - **Mudança:**
     - `.ie-quadrado .ie-destaque { width:100%; height:100%; border:0 }`
     - `.ie-quadrado .ie-destaque::after { inset:64px; border-width:6px }`
     - `.ie-quadrado .ie-destaque span { font-size:560px }`
     - Na prévia, uma artboard 1080 real ao lado das miniaturas.

8. **P2: ajustar os limites da lista.**
   - **Onde:** CarrosselLista/README.md:3-4; bundle.css:137-146.
   - **Problema (verificado, T4Lista.png):** 5 itens com 10 palavras de explicação, mais o fecho, estouram 132px abaixo da arte.
   - **Mudança:** limitar a "3 ou 4 itens com até 8 palavras de explicação; 5 itens só sem explicação", ou criar `.ie-lista.ie-compacta { gap: var(--space-3) } .ie-lista.ie-compacta li { padding-top: var(--space-3) }`.

9. **P2: levar os tamanhos para os tokens.**
   - **Onde:** tokens.json:48; MioloDeclaracao/README.md:5; previews com `style="font-size:150px|156px"`; bundle.css (literais).
   - **Problema (verificado):** `capa` diz "só no primeiro slide, no estático e no story", mas a Declaração usa `capa` a 156px. 150 e 156 não existem nos tokens.
   - **Mudança:**
     - Criar `capa-media` (150px) e usá-lo também na Declaração, aposentando o 156.
     - Criar `gigante` (420), `numeral-xl` (560), `numeral-md` (168) e `aspas` (360), e remover os `font-size` literais do bundle.css.
     - Atualizar o `usage` de `capa`.

10. **P2: resolver o marfim duplicado e o termo indefinido.**
    - **Onde:** README.md:37, 127, 198; FechamentoEspelho/README.md:3-5 e preview.html:7.
    - **Problema (verificado):** o Espelho de C4 cria um segundo slide com marfim, contra a proibição de "mais de um slide marfim". "Carrossel alternado" não está definido.
    - **Mudança:**
      - Escrever "o Espelho de C4 é o único outro slide com marfim; nesse carrossel não há Pausa", ou fazer o topo do Espelho em `superficie` Noite.
      - Trocar "só em carrossel alternado" por uma condição verificável: "só com capa escura e carrossel de 8 slides ou mais".

11. **P2: tirar os botões desenhados do story e do estático.**
    - **Onde:** Story/README.md e preview.html:15; CTA/README.md:5-6; README.md:177-178.
    - **Problema (verificado):** o Story desenha "Ver o carrossel", que não é clicável, pela mesma razão que o StoryInterativo proíbe desenhar o sticker. O CTA recomenda `ie-botao` no estático, que está no feed. O README diz que o story leva `ie-logo-md`, e o Story não tem logo.
    - **Mudança:**
      - O Story de divulgação passa a ser "compartilhar o post no story" (o card fica clicável) sobre um fundo do sistema, com `ie-guia-sticker` reservando cerca de 640 × 800 no centro, ou com um sticker de link real.
      - Remover o `ie-botao` do estático: lá a ação vai em `ie-chave`.
      - Decidir se a logo vai no story e alinhar README e prévia.

12. **P2: criar a seção "Quando falta algo".**
    - **Onde:** README.md (seção nova) e Briefing.md:7-17.
    - **Mudança:**
      - Sem foto real: use C5 ou `MioloCitacao` assinada. Nunca rosto gerado por IA, nunca banco de imagem.
      - Sem número com fonte: use `MioloContraste` ou `MioloDeclaracao`, sem numeral.
      - Sem permissão do cliente: não publique prova.
      - Acrescentar ao briefing o campo "Fotos disponíveis".

13. **P2: corrigir a conta de texto grande.**
    - **Onde:** tokens.json:30 (`ouro-escuro`); README.md:166-170.
    - **Problema (verificado):** "texto de 24px ou mais (4.3:1)" aplica a exceção WCAG de texto grande ao pixel da arte. Mas 24px na arte viram cerca de 8,7pt no celular; texto grande na tela (24 CSS px) equivale a cerca de 66px na arte.
    - **Mudança:**
      - Reescrever a nota: "como texto, só a partir de 66px na arte".
      - Pôr no README a conversão "px da arte × 0,36 ≈ pt no celular".
      - Tirar "Arraste para o lado" do exemplo de alt text (Legenda.md:39): é ruído para leitor de tela.

14. **P2: criar o ciclo de medição e a mensagem da DM.**
    - **Onde:** Linha-editorial.md (seção nova); Legenda.md:47-50.
    - **Mudança:**
      - Tabela de objetivo, métrica e meta:
        - Alcance: envios ÷ alcance e % de não seguidores alcançados.
        - Valor: salvamentos ÷ alcance.
        - Conversa: comentários com a palavra e DMs abertas.
      - Revisão a cada 9 posts: troque pilar ou tipo de gancho do pior terço.
      - Texto padrão da DM de "Diagnóstico": abertura, uma pergunta de qualificação e o link de agenda.

15. **P2: ampliar a cobertura de formatos.**
    - **Onde:** README.md:62, 91-100; tokens.json `formato`.
    - **Mudança:**
      - Permitir C1 a C7 como estático, com `ie-logo-sm`.
      - Criar `StoryAbertura`, `StoryRepost`, `CapaReels` Marfim, `AnuncioFeed` (4:5) e `AnuncioVertical` (9:16).
      - Adicionar `anuncio-topo: 270px` (14% da Meta) e `anuncio-lateral: 65px` (6%). Hoje só a base de anúncio é citada.
      - Orientar o avatar (monograma) e a bio.

16. **P3: especificar vídeo e movimento.**
    - **Onde:** README.md:88; ReelsTexto/README.md; Briefing.md:43.
    - **Mudança:**
      - Dizer o que o Claude entrega: camadas PNG nomeadas `NN-reels-gancho.png` e `NN-reels-legenda-MM.png`, mais o roteiro com timecodes.
      - Tempo por bloco de legenda (cerca de 1,2 a 2,5 s) e entrada e saída do gancho.
      - Exportação em 1080 × 1920 e 30 fps (confirmar no app).
      - Desligar a legenda automática do Instagram quando houver legenda queimada, para não duplicar.

17. **P3: corrigir a consistência miúda (todos verificados).**
    - CapaPalavra/README.md:3 dá "esfriou" (7 letras) como exemplo e a linha 4 limita a 6. O render T1Esfriou mostra que 7 cabem: suba o limite para 7.
    - tokens.json:58 diz que `lead` é para itens de checklist, mas `MioloChecklist` usa `item`: corrija o `usage`.
    - CarrosselRetrato/preview.html:14 tem um número sem fonte: acrescente `nota` com fonte e período ou tire o número.
    - `CarrosselMarca` usa `ie-brilho-centro` num slide de miolo, contra README.md:78 e tokens.json:97: registre a exceção.
    - A diagonal da `CapaMarfim` não cruza a borda, contra README.md:79.
    - `MioloProva` exige o rótulo "Resultado", mas README.md:132 diz que "número" não leva rótulo: defina se Prova é exceção.
    - `SeloSerie` diz "episódio" e o registro usa o número global: escolha um.
    - O exemplo do Briefing tem os slides 5, 6 e 7 em `ie-base`: troque o 5 por `MioloChecklist` (`ie-centro`) ou ancore a Grade no topo.
    - `CarrosselRetrato` permite 35 palavras de corpo, mais título e papel, o que passa de 40 (README.md:28): baixe para 28.

18. **P3: ajustes de conformidade com o formato.**
    - Tirar as notas de versão dos `usage` (tokens.json:13 "Adição do v2", :32 "Adição do 2.0", :28 "do sistema anterior").
    - No passo 5 (README.md:18), mandar usar o `tokens.css` que o sistema publica, gerado de tokens.json, em vez de compilar à mão.
    - No Cover (Cover/preview.html:20), pôr o nome em `tinta`: cover.md pede o nome em ink, e "Elite" está em itálico dourado.
    - Completar a tabela "Classes, de relance" (README.md:102-113) com `ie-destaque`, `ie-perfil`, `ie-perfil-tile`, `ie-dividida-topo/base`, `ie-moldura`, `ie-cartao-num`, `ie-contraste-lado/fio`, `ie-barra*`, `ie-foco`, `ie-eu`, `ie-balao-hora` e `ie-alerta`.
    - Conferir se `project/design-system.json` deve ficar dentro de `project/`: format.md:17 lista `design-system.json` entre os caminhos reservados.
