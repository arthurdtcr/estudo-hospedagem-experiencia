# Impulse Elite: cópia versionada do Design System

O Design System vivo está no Claude: https://claude.ai/artifact/9eggYVve7p8i6mN5X71wRe

Esta pasta guarda uma cópia dos arquivos `project/` publicados ali, para histórico e revisão.

- `project/`: o sistema (README, seções, tokens, componentes). É o que o Claude lê.
- `pesquisa.md`: o contexto do Instagram em 2026 usado nas decisões, com fontes.
- `juiz/`: os relatórios do juiz independente, rodada a rodada, com a nota de cada versão.
- `tools/`: `compile_tokens.py` (valida `tokens.json`, gera `tokens.css` e mede contraste), `render.js` (renderiza cada prévia como o Claude faria) e `sheet.py` (monta pranchas de contato).

Para revalidar: `python3 -I tools/compile_tokens.py project /tmp/tokens.css`.
