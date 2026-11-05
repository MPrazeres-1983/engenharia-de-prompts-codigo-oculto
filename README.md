# O Código Oculto da Inteligência Artificial

**Mário Prazeres — terceira edição em desenvolvimento, 5 de novembro de 2026.**

Esta branch amplia *Engenharia de Prompts: O Código Oculto* para fundamentos, utilização criativa, sistemas, operação e impacto social da IA. O título é provisório. **O manuscrito ainda não satisfaz a ambição editorial final e não está aprovado para publicação ou merge.**

A estrutura de trabalho tem dez partes, 50 capítulos, três apêndices, 74 laboratórios, 93 referências e 58 entradas de glossário. O guia de consulta liga pontos de entrada para tarefas concretas aos capítulos de aprofundamento. Os 17 capítulos revistos no checkpoint I completam a passagem editorial por todos os capítulos. Os resultados e a ordem de retoma estão na [ancoragem](docs/V3_ANCORAGEM.md).

O [projeto criativo A Meia Testemunha](exemplos/atelier/README.md), o caso SyRI e o [ensaio de cache](experiencias/operacao/README.md) integram a edição. A leitura independente e os ensaios pendentes têm critérios de fecho próprios.

A segunda edição permanece em `main@975ade89632700918786603dc23722e74f8610f7`, integrada pelo [PR #1](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/1). Esta revisão usa `terceira-edicao-ia-referencia-2026` e o [PR #2, Draft](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2). Não cria tags ou releases nem altera diretamente `main`.

## Estado, fontes e revisão

- [Plano e três alternativas de título](docs/V3_PLANO_EDITORIAL.md)
- [Progressão, narrativa e contrato factual](docs/V3_LINHA_NARRATIVA.md)
- [Ancoragem da retoma e estado dos blocos](docs/V3_ANCORAGEM.md)
- [Auditoria dos 29 capítulos e mapa de lacunas](docs/V3_MATRIZ_COBERTURA.md)
- [Progresso, pendências e próximo passo exato](docs/V3_PROGRESSO.md)
- [Fontes e alcance da consulta V3](docs/V3_FONTES_E_EVIDENCIAS.md)
- [Validação e limites](docs/V3_VALIDACAO.md)
- [Manifesto de estrutura](docs/V3_ESTRUTURA.json)
- [Documentação histórica da segunda edição](docs/VALIDACAO_SEGUNDA_EDICAO.md)

O PDF e as evidências são guardados nos [artefactos de Actions](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/workflows/main.yml), com a revisão compilada. A folha de rosto indica o título provisório e a nota distingue o estado de trabalho da publicação definitiva. A capa original é preservada.

## Compilar e verificar

Requer TeX Live com padrões de hifenização de português, pdfLaTeX, latexmk, BibTeX, TikZ, natbib e tcolorbox. O Babel importa o locale português incluído. Em Ubuntu/Debian, os conjuntos `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-lang-portuguese`, `texlive-science` e `latexmk` cobrem as dependências usuais.

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error src/livro.tex
python3 scripts/verificar_livro.py --log src/livro.log
python3 -m unittest discover -s tests -v
python3 -m compileall -q exemplos scripts tests experiencias
```

O manifesto verifica dez partes, ordem dos capítulos e apêndices, laboratórios, labels, citações e JSON. Não certifica qualidade científica ou legibilidade. O log rejeita overfulls, referências indefinidas e outros erros relevantes; a revisão visual é um passo separado.

## Laboratórios offline

Python 3.10+, apenas biblioteca padrão, sem rede ou chaves:

```bash
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Estado LAV-001"
python3 -m exemplos.lavandaria.avaliar
python3 -m exemplos.laboratorio.fundamentos
python3 -m exemplos.laboratorio.decisoes
python3 -m exemplos.laboratorio.adaptacao
python3 -m exemplos.laboratorio.skills
python3 -m exemplos.laboratorio.equipas
python3 -m exemplos.laboratorio.operacao
python3 experiencias/equipas/offline.py --verificar
python3 experiencias/llm_local/verificar_registo.py
```

A [Lavandaria](exemplos/lavandaria/README.md) é fictícia e usa pesquisa lexical, templates, contratos e autorização. Os fundamentos executam cálculos didáticos de regressão, atenção, quantização e memória. O [pacote de skill](exemplos/skills/rever-evidencias/SKILL.md) tem validador estrutural e recursos com hashes; esses controlos não verificam verdade factual nem ativação num produto.

O controlador de equipa, por omissão, usa um **stub determinístico**. O ensaio offline acerta dois de quatro casos nos três modos; a equipa executa mais componentes sem acrescentar capacidade ao mesmo stub. Isto não mede desempenho de um LLM.

Os cálculos de decisão distinguem sensibilidade e valor preditivo, redução do tempo e aumento da produção por tempo, e energia estimada e medida. A [adaptação linear](experiencias/adaptacao_linear/README.md) treina um adaptador de posto um sobre uma matriz 2×2 congelada, com resultado e código identificados. Inclui um alvo representável e outro que conserva erro por limite de capacidade. É uma experiência matemática executada; não é fine-tuning de LLM. O conjunto completo tem **76 testes aprovados** na validação deste ciclo, incluindo seis para o incidente de cache.

## Inferência real e bloqueio atual

As [52 inferências reais da segunda edição](experiencias/llm_local/README.md) estão preservadas, com respostas brutas, configuração e resultados negativos. A CI reavalia integridade; não volta a executar o modelo.

O [novo piloto V3](experiencias/equipas/README.md) está implementado, com quatro casos e 32 chamadas de modelo planeadas. **Não foi executado com LLM:** a cópia disponível do modelo estava incompleta, e ambas as tentativas de obter outra cópia falharam por timeout. Não há medições com participantes humanos ou treino LoRA/QLoRA de um LLM. O ateliê tem uma curta muda de quinze segundos e um cartaz exportados. Outras extensões multimédia e a avaliação com espectadores estão propostas nos laboratórios.

## Organização, autoria e licença

`src/livro.tex` determina a ordem; os prefixos numéricos dos ficheiros conservam identidade histórica. `src/preambulo.tex` contém os estilos e `src/referencias.bib` a bibliografia. `docs/` conserva decisões e checkpoints; `exemplos/`, `experiencias/`, `scripts/` e `tests/` fornecem o companheiro executável.

Mário Prazeres, licenciado em Engenharia Informática. Obra sob [CC BY-NC-SA 4.0](LICENSE). A assistência de IA é declarada na nota editorial. Licenças de modelos e bibliotecas permanecem próprias; pesos não são redistribuídos no repositório. Título comercial, capa final, publicação e merge dependem de decisão do autor.
