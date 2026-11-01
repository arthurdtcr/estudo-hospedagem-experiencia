# Carrosséis Impulse Performance (15)

Pedido do Arthur (01/11/2026): 5 carrosséis que seguem o carrossel de apresentação
(https://claude.ai/artifact/HvuBQG3AmoDzAA2g2fEVAg), depois mais 10 com o mesmo método. Cada um sobe um nível de
consciência (Schwartz). Método por roteiro: rascunho > 5 reanálises > pesquisa de persuasão > 6ª reanálise > crítico
independente (subagente) > filtro > 7ª reanálise > construção no Claude Design com o Design System Impulse Elite.
**Tudo isso já foi feito para os 15.** Hospedagem de experiência NÃO é mais o nicho: não usar.

## Índice
| # | Carrossel | Ação | Canvas |
|---|---|---|---|
| 01 | [Ele quase comprou de você](01-ele-quase-comprou-de-voce/README.md) | Enviar | https://claude.ai/artifact/AYNJe4hyWHa47FMVBdzmrU |
| 02 | [Seu cliente não sumiu. Esfriou.](02-seu-cliente-nao-sumiu-esfriou/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/7HsXetiyaUu1NLgoGWJJyw |
| 03 | [Antes de te chamar, ele te confere](03-antes-de-te-chamar-ele-te-confere/README.md) | Salvar | https://claude.ai/artifact/KrHHxd6EDGjvvY4gzFVZ1n |
| 04 | [Dobrar a verba não dobra as vendas](04-dobrar-a-verba-nao-dobra-as-vendas/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/UtcRgSTM8rQA8DPfF2Vz7o |
| 05 | [Diagnóstico de graça? Qual é a pegadinha?](05-diagnostico-de-graca-qual-e-a-pegadinha/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/9DL6ALxBy99BgTjXCPbAiM |
| 06 | [Indicação não tem botão de ligar](06-indicacao-nao-tem-botao-de-ligar/README.md) | Enviar | https://claude.ai/artifact/NuwkexHUr4ndVxNpmsPCRL |
| 07 | [Já investi em anúncio. Não funcionou.](07-ja-investi-em-anuncio-nao-funcionou/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/3N9f92AykyFfNH4PoHqLq7 |
| 08 | [Seu relatório mostra cliques. E os clientes?](08-seu-relatorio-mostra-cliques-e-os-clientes/README.md) | Salvar | https://claude.ai/artifact/R2VopuvsdWj2aZrMZBu4rm |
| 09 | [De onde veio a sua última venda?](09-de-onde-veio-a-sua-ultima-venda/README.md) | Salvar | https://claude.ai/artifact/FaVD7E6KRquZVKMFH1dNiq |
| 10 | [Impulsionar não é anunciar](10-impulsionar-nao-e-anunciar/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/43DCSWzixAgBjX4sYUYc3S |
| 11 | [Google ou Instagram?](11-google-ou-instagram/README.md) | Comentar onde anuncia | https://claude.ai/artifact/3CYPFzTWK94cSUvorAgKx4 |
| 12 | [Quanto investir em anúncio? Comece pela conta.](12-quanto-investir-em-anuncio-comece-pela-conta/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/RRJeoQwdgofT6dD3eYMvpP |
| 13 | [Em quanto tempo o anúncio dá resultado?](13-em-quanto-tempo-o-anuncio-da-resultado/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/5Npe1zNbFAXfXHrQnn1y1A |
| 14 | [Cinco perguntas antes de contratar uma agência](14-cinco-perguntas-antes-de-contratar-uma-agenci/README.md) | Salvar | https://claude.ai/artifact/EAJRC9spcyPXFV2W1MuwLV |
| 15 | [A resposta pode ser: ainda não anuncie](15-a-resposta-pode-ser-ainda-nao-anuncie/README.md) | Comentar Diagnóstico | https://claude.ai/artifact/MSRaVvuxDK6imR8kWTfzf9 |

Cada pasta tem `README.md` (roteiro final legível, legenda, pendências), `roteiro.json` (fonte da verdade) e, nos 6 a 15,
`canvas/` (arquivos prontos para publicar) e `previa.png` (folha de prévia).

## Estado e o que falta
1. **Os 15 carrosséis estão publicados no Claude Design** (links no índice). Os canvases são privados: para mostrar a
   alguém, compartilhe pelo menu Share de cada um.
2. **Push para o GitHub** falha com 403 (sem acesso ao repositório). Commits só locais até o Arthur reconectar o GitHub
   em https://claude.ai/connect-github.
3. **Pendências do Arthur** (estão no README de cada carrossel): fluxo do diagnóstico (C5), conta no nome do cliente (C14),
   "cada diagnóstico passa pela minha mão" (C15), frases em primeira pessoa das legendas, foto P&B (C5 e C15).

## Como publicar um canvas pronto (para carrosséis novos)
- Tipo Design: `https://claude.ai/artifact/QKN21svewxgyPb6SYRqWnd`. Criar: Artifact publish com `type_url` desse tipo,
  `title` = o `title` do `canvas/project/canvas.json`, `auto_open: "after_first_write"`.
- Depois, com o `url` devolvido e `root` = a pasta `canvas/` do carrossel: primeiro publish com `file_path` =
  `canvas/project/canvas.json` e `files` = `project/Main.dc.html` mais o Design System copiado pelo servidor:
  `project/ds/impulse-elite/tokens.json` = {artifact: DS, path: project/tokens.json},
  `project/ds/impulse-elite/components/bundle.css` = {artifact: DS, path: project/components/bundle.css},
  `project/estilo/tokens.css` = {artifact: https://claude.ai/artifact/HvuBQG3AmoDzAA2g2fEVAg, path: project/estilo/tokens.css}.
  (As cópias locais desses três arquivos também estão em `canvas/project/`.)
- Depois, um publish por slide (`Slide02.dc.html`, `Slide03.dc.html`...), na ordem do `canvas.json`.
- Design System Impulse Elite: `https://claude.ai/artifact/9eggYVve7p8i6mN5X71wRe` (versão 1793507287-6e32, namespace
  `impulse-elite`). Sem logo em carrossel de conteúdo.

## Regras que valem para qualquer carrossel novo
Ver `ferramentas/contexto-da-marca-para-criticos.md` (marca, persona, voz do Arthur, restrições do DS, fatos
verificados) e `processo/serie-1/04-o-que-veio-do-drive.md`. Resumo: máx. 40 palavras por slide contando rótulo e fecho;
uma ênfase por slide; nunca travessão; número só com fonte; "a gente" nos slides, "eu" só no slide do fundador e na
legenda inteira; concordar antes de virar; legenda com 2 linhas de gancho, follow antes da palavra-chave, palavra-chave
por último; ação padrão "Comente Diagnóstico".

## Ferramentas
- `ferramentas/gerar.py`: gera `canvas.json` e cada `.dc.html` a partir de um `roteiro.json`
  (`python3 gerar.py <json com lista de carrosséis> <id> canvas|<n_slide> <pasta>`).
- `ferramentas/previa.js`: renderiza PNG de cada slide com Playwright (`node previa.js <pasta com canvases> <saída>`).

## Processo registrado
`processo/serie-1/` e `processo/serie-2/`: rascunhos, as reanálises, pesquisa (fontes e como cada uma entrou), as críticas
completas dos subagentes e o filtro (aceito e rejeitado, com motivo).
