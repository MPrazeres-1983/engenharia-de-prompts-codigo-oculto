# Validação da terceira edição

Data: 04-11-2026. Este ficheiro distingue a base existente das alterações V3.

## Base, antes de alterações ao manuscrito

| Verificação executada | Resultado |
|---|---|
| Árvore local vs `main@975ade8` | `13de7f25f76d803ed5f68878b6cab804727fd985`, idêntica |
| `python3 -m unittest discover -s tests -v` | 30 testes passaram |
| `python3 scripts/verificar_livro.py` | 29 capítulos, 47 laboratórios, 41 referências, zero erros |
| `python3 experiencias/llm_local/verificar_registo.py` | 52 registos, hashes e métricas consistentes |

Não foi necessária nova execução das 52 inferências históricas. A segunda edição tem evidência de CI no PR #1; essa evidência não valida alterações V3 ainda não produzidas.

## V3

Compilação, novos testes, inspeção visual e GitHub Actions: pendentes neste checkpoint. Os resultados finais serão acrescentados depois da execução, com SHA e comandos. Não existem resultados simulados apresentados como medições.

## Critérios editoriais de aceitação

As dez áreas precisam de conteúdo real, progressão, exemplos e fontes. A matriz inicial identifica lacunas; a matriz final deve indicar o que foi efetivamente resolvido e o que precisa de aprofundamento. O manuscrito só se declara pronto para revisão integral quando essas condições forem confrontadas com o texto produzido. A revisão humana e a decisão de publicação mantêm-se separadas da verificação automatizada.
