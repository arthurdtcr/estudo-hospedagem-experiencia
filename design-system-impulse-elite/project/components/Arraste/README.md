Arraste e costura: a dica de deslizar da capa. O filete sai pela borda direita e entra pela borda esquerda do slide 2, na mesma altura.

- **Use quando:** em toda capa de carrossel (`ie-arraste`) e no slide 2 (`ie-costura`) quando a capa não é C5 (lá o filete é curto e não sai pela borda) e a base esquerda do slide 2 está livre.
- **Você fornece:** nada além da palavra "Arraste".
- **Estrutura:** `<div class="ie-arraste"><span>Arraste</span></div>` como último item da área da capa; o filete se estende sozinho até a borda. No slide 2, `<span class="ie-costura"></span>` como primeiro filho da `ie-arte`. Em capa centralizada (C5), o filete fica curto, ao lado da palavra.
- **Não faça:** seta, mão, emoji ou indicador "1/8"; costura quando o slide 2 tem texto na base esquerda.
