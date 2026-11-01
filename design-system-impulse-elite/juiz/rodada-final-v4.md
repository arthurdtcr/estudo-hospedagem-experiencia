# Impulse Elite v4: nota final

O que eu verifiquei:
- Comparei a v4 com a cópia da v3 que guardei (`juiz/r2/teste/`).
- `compile_tokens.py`: nenhum erro de gramática, 24 pares de contraste OK, e o `tokens.css` dos renders da v4 bate com o compilado.
- Conferi as 7 receitas contra a tabela de âncoras (README.md:106-114) e contra as regras de Pausa, dado e costura.
- Rodei dois testes de estresse nos componentes novos, em `juiz/final/out/final-stress.png`. Não toquei em `ds/`.

## 1. Os 14 pontos da rodada 2

1. **Histórico no briefing: resolvido.** O briefing ganhou a linha "Histórico" (Briefing.md:18). O registro também vai para um arquivo da equipe (README.md:24), e sem registro basta perguntar só a última capa (README.md:37), não usar capa clara sempre.
2. **Janela forçada para Reels e estático: resolvido.** README.md:165-168 dá a saída por formato. `CapaReelsMarfim` existe. Na forma C6, o estático fica sem logo (Estatico/README.md).
3. **Âncora por composição: resolvido.** Há uma tabela em README.md:106-114 e uma linha "Âncora:" em 19 READMEs. Apresentação e Dado foram reordenadas, e nenhuma das 7 receitas tem três âncoras iguais seguidas. A única simplificação é "a capa conta como base".
4. **Fallback dentro da receita: resolvido.** A coluna "Na receita" está em README.md:41-51, seguida de "confira a âncora". Objeção sem foto (Retrato vira Pergunta, topo) passa na regra.
5. **README da logo: resolvido.** `assets/Logos/README.md:3-4` e README.md:232-233 agora dizem a mesma coisa.
6. **Prévias do CTA e do ReelsTexto: resolvido.**
   - O CTA mostra as três `ie-chave` e põe o `ie-botao` sob "Fora do Instagram".
   - O ReelsTexto usa `ie-transparente`, `body` transparente e o quadro de vídeo fora da artboard.
7. **Legenda por preset do editor: resolvido.** Está em ReelsTexto/README.md e README.md:130. O PNG por bloco ficou como exceção.
8. **Contradição de pilar e métrica: resolvido.**
   - O conflito de pilar foi desfeito em Linha-editorial.md:19-20.
   - A métrica de apoio do carrossel virou "visitas ao perfil".
   - A anotação é feita 7 dias depois, num formato definido (linhas 37, 42 e 46).
9. **Anúncio de feed: resolvido.** `AnuncioFeed` é uma capa sem "Arraste", sem logo e sem @, e está em README.md:90.
10. **Capa de Reels escura: resolvido.** O título agora é `capa`, ancorado no centro. Na `GradePerfil` ela tem o mesmo peso das capas de carrossel.
11. **Ganchos de Reels: resolvido.** Ganchos.md:41-58 traz fala e texto na tela por tipo de gancho e a estrutura de 30 a 45 s.
12. **Exceções e usos: resolvido.**
    - A ação do estático e do Reels fica só na legenda (README.md:203, 246).
    - O horário passou a 28px e saiu da lista de `nota`.
    - Os `usage` de `capa`, `brilho` e `nota` foram corrigidos, e o tema virou "Marfim".
    - Briefing e Legenda citam as três capas de Reels, e CarrosselPausa traz as 3 condições.
    - Resta só um resíduo trivial novo: o cabeçalho "Miolo (14)" em README.md:175, quando agora são 15.
13. **Story: resolvido.** O fluxo virou previsível: PNG publicado como story, miniatura da capa e sticker de link (560 × 140). Há variante para link externo, e o README explica por que não usar o compartilhamento nativo.
14. **`design-system.json`: resolvido, e não era problema.** O artefato publicado que foi baixado tem `project/design-system.json` (`artifact-files/.../project/design-system.json`). A lista de format.md:17 vale para a tabela de uma página de arquivo único. Retiro a ressalva das rodadas 1 e 2.

Saldo: 14 de 14 resolvidos. Os dois testes de estresse passaram:
- `CapaReelsMarfim` com 6 palavras cabe abaixo de 1480, mas ocupa 4 linhas, contra "até 3 linhas" no README: limite de palavras e de linhas não batem.
- `MioloPergunta` com a pergunta em 3 linhas ainda cabe no bloco de cima.

## 2. Nota final: 8.4/10

| # | Critério (peso) | v2 | v3 | v4 |
|---|---|---|---|---|
| 1 | Cobertura de formatos (12%) | 7.0 | 7.9 | 8.4 |
| 2 | Precisão técnica 2026 (12%) | 7.0 | 8.0 | 8.3 |
| 3 | Operabilidade por IA (20%) | 6.5 | 7.4 | 8.4 |
| 4 | Identidade e qualidade visual (15%) | 7.7 | 7.8 | 8.0 |
| 5 | Acessibilidade e legibilidade (8%) | 7.0 | 8.0 | 8.3 |
| 6 | Estratégia de conteúdo (12%) | 7.5 | 8.0 | 8.5 |
| 7 | Consistência interna (13%) | 5.8 | 7.0 | 8.4 |
| 8 | Conformidade com o formato (8%) | 8.2 | 8.7 | 9.0 |
| | **Nota ponderada** | **7.0** | **7.8** | **8.4** |

Conta da v4: 8.4×0.12 + 8.3×0.12 + 8.4×0.20 + 8.0×0.15 + 8.3×0.08 + 8.5×0.12 + 8.4×0.13 + 9.0×0.08 = 1.008 + 0.996 + 1.680 + 1.200 + 0.664 + 1.020 + 1.092 + 0.720 = **8.38, arredondado para 8.4**.

## 3. O que separa esta versão de um 10

Como sistema de regras, o Impulse Elite agora é sólido: determinístico, coerente entre arquivos e honesto sobre o que estima. O que falta para um 10 está fora do texto:

- **Faltam os materiais.** Não há nenhuma foto real do Arthur, de bastidor ou de cliente, nem vídeo. As peças mais persuasivas (C7, Retrato, prova com cliente, Reels com rosto) só existem como placeholder, e o feed real tende ao "cartão de frase" escuro, elegante mas repetitivo no miolo.
- **As regras não têm verificador.** São perto de dez restrições que interagem (janela, não repetir, âncora, Pausa, dado, rótulo, costura, palavras por slide), e o agente confere tudo de cabeça, a partir de prosa. Um 10 teria essas regras numa forma checável (uma tabela ou script de validação do roteiro) e limites de texto que batem com a geometria: "6 palavras" e "3 linhas" já divergem na `CapaReelsMarfim`.
- **O sistema não foi validado na prática.** As zonas seguras e os nomes de métricas são estimativas com ressalva. Os pilares saem de 15 posts, e nenhuma receita ou tipo de gancho foi testado contra o Insights da conta. O histórico ainda depende de a equipe manter o arquivo de registro.
- **Faltam formatos menores:** colab, capa de Live, canal de transmissão e carrossel com foto ou vídeo real.

Nada disso impede o uso hoje. É a distância entre "pronto e bem pensado" e "comprovado em produção".
