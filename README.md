# Engenharia de Prompts: O Código Oculto

**Mário Prazeres — segunda edição (3 de novembro de 2026).**

O livro começa sem exigir conhecimentos técnicos e avança até modelos, raciocínio, software, RAG, ferramentas, agentes, avaliação, segurança e governação. Mantém a capa e a identidade da primeira edição. A revisão tem 29 capítulos, três apêndices, 47 laboratórios e bibliografia BibTeX.

A segunda edição é integrada em `main` pelo [PR #1](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/1), com autorização expressa do autor. A primeira edição permanece no histórico em `f63d417fb655c6af013569c5381235625e0567d1`. O merge não cria tags ou releases automaticamente.

## Ler e rever

O PDF e as evidências de teste são guardados nos [artefactos de GitHub Actions](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/workflows/main.yml). Escolhe a execução da branch e o commit pretendidos; cada PDF identifica a revisão compilada. O índice paginado é gerado pelo LaTeX.

- [Auditoria integral](docs/AUDITORIA_EDITORIAL.md)
- [Estrutura e plano editorial](docs/PLANO_SEGUNDA_EDICAO.md)
- [Guia de escrita e terminologia](docs/GUIA_EDITORIAL.md)
- [Alterações e mapeamento por capítulo](docs/CHANGELOG_SEGUNDA_EDICAO.md)
- [Fontes e alcance da verificação](docs/FONTES_VERIFICADAS.md)
- [Laboratórios](docs/LABORATORIOS.md)
- [Validação e questões para revisão humana](docs/VALIDACAO_SEGUNDA_EDICAO.md)
- [52 inferências reais: prompts, respostas, métricas e falhas](experiencias/llm_local/README.md)

## Compilar

Requer TeX Live com português, pdfLaTeX, latexmk, BibTeX, TikZ, natbib, tcolorbox e os pacotes habituais de LaTeX. Não usa Biber ou shell escape.

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error src/livro.tex
python3 scripts/verificar_livro.py --log src/livro.log
```

Em Ubuntu/Debian, os conjuntos `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-lang-portuguese`, `texlive-science` e `latexmk` cobrem as dependências usuais. A Actions existente foi adaptada para compilar e verificar o projeto em pushes e pull requests.

## Executar os exemplos

Python 3.10+, apenas biblioteca padrão:

```bash
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Estado LAV-001"
python3 -m exemplos.lavandaria.avaliar
python3 -m unittest discover -s tests -v
python3 scripts/verificar_livro.py
```

[A Lavandaria das Meias Desaparecidas](exemplos/lavandaria/README.md) é um caso fictício com pesquisa lexical, templates, contratos e autorização. Não executa um LLM, não implementa MCP e não precisa de rede ou chaves. Os dois scripts históricos foram corrigidos para identificar claramente as heurísticas e retirar confiança inventada.

O [ensaio opt-in com Qwen2.5-0.5B e llama.cpp](experiencias/llm_local/README.md) acrescenta inferência real, com configuração fixada e todas as saídas guardadas. Não altera a demonstração offline nem corre na CI. Os resultados incluem falhas de classificação, cálculo e conteúdo, mesmo em JSON válido.

## Organização

`src/livro.tex` é a entrada; `src/preambulo.tex` contém a apresentação; `src/capitulos/` organiza o manuscrito; `src/referencias.bib` guarda fontes. `exemplos/`, `tests/` e `scripts/` contêm demonstrações e verificações; `docs/` regista a revisão.

## Autor e licença

Mário Prazeres, licenciado em Engenharia Informática. Obra sob [CC BY-NC-SA 4.0](LICENSE). A nota de edição declara a assistência de IA e mantém a aprovação final a cargo do autor.
