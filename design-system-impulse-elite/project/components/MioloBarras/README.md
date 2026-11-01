Barras: um dado comparado em até 4 barras horizontais. A barra que importa em `destaque`, as outras em `tinta-suave`, a ponta cortada pelo chanfro.

- **Use quando:** o argumento depende de uma proporção (cliques contra vendas, canal contra canal).
- **Você fornece:** título, de 2 a 4 linhas com nome (`corpo`), valor real e `--valor` (0 a 1, proporcional à maior), a barra em foco (`ie-foco`) e a fonte com período em `nota`.
- **Estrutura:** `ie-barras` > `ie-barra` > nome + `ie-barra-linha` > `<span class="ie-barra-fio" style="--valor:0.34"></span>` + `ie-barra-valor`.
- **Âncora:** base.
- **Não faça:** número sem fonte; mais de uma barra em `ie-foco`; eixo, grade ou legenda de cores (o nome está na própria barra). Os `000` da prévia são lugar de número real.
