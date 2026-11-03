# Validação da segunda edição

Revisão de trabalho de **3 de novembro de 2026**, na branch `segunda-edicao-2026`. A primeira edição permanece em `main@f63d417fb655c6af013569c5381235625e0567d1`. Não foi feito merge, criada tag ou publicada edição definitiva.

## Resultado local

| Verificação | Resultado |
|---|---|
| Compilação original, depois de instalar a dependência portuguesa local | 164 páginas; 33 avisos de largura. |
| Compilação revista com pdfLaTeX + latexmk + BibTeX | 198 páginas, sem erros, referências/citações indefinidas ou avisos relevantes de composição. |
| Estrutura | 29 capítulos, três apêndices, 47 laboratórios, 38 entradas bibliográficas. |
| Instâncias JSON nas listagens identificadas como objetos | 4 válidas; restantes listagens são prompts, comandos ou formatos explicitamente ilustrativos. |
| Testes Python | 30 passaram, 0 falharam. |
| Regressões offline da Lavandaria | 12/12 condições conhecidas verificadas. Não são estimativa de desempenho de LLM. |
| Sintaxe Python | `compileall` sobre exemplos, scripts e testes passou. |
| Capa | SHA de blob original `abf61605f1a89e2bbed54659c1564c2376dbb3c4`, preservado. |
| Segurança da consulta | Casos autorizados funcionam; acesso cruzado negado; campo de identidade proposto rejeitado. |
| Evidência e contratos | Campo extra, tipo incorreto, ID trocado, fonte inventada e excerto falso/vazio rejeitados. |
| Exemplo matemático | Wilson para 8/10: `[0.4901624715, 0.9433178485]`; hipóteses e limites no capítulo 25. |

Comandos reproduzíveis, na raiz:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error src/livro.tex
python3 scripts/verificar_livro.py --log src/livro.log
python3 -m unittest discover -s tests -v
python3 -m exemplos.lavandaria.avaliar
python3 -m compileall -q exemplos scripts tests
```

O validador de contrato é específico desta demonstração; não se apresenta como motor genérico de JSON Schema. O módulo opcional `jsonschema` não estava instalado no ambiente de execução e não foi necessário para a suite. O esquema é JSON válido e as restrições concretas relevantes são verificadas em código e nos testes negativos.

## Inspeção editorial e visual

Leitura integral da versão original e revisão do texto alterado. A auditoria regista problemas por capítulo e o changelog liga a numeração original à nova. As principais remoções correspondem a afirmações sem suporte, números retóricos, fórmulas ilegíveis e JSON inválido; a justificação está registada.

Inspeção global de todas as páginas em folhas de miniaturas, com ampliação de capa, índice, abertura de capítulos, fórmulas, diagramas de Transformer/RAG/ferramentas/avaliação, tabelas, laboratórios, glossário e bibliografia. Uma verificação de coordenadas não encontrou texto fora dos limites de página. Foram corrigidas a proximidade da anotação no Transformer, a passagem do esquema a uma página isolada, uma linha demasiado larga e a largura de etiquetas no glossário. A capa mantém o seu enquadramento original.

Uma inspeção por amostragem não substitui prova tipográfica linha a linha nem experiência com leitores. O manuscrito continua identificado como revisão de trabalho.

## GitHub Actions

A workflow existente foi adaptada para push e pull request, validação estática, testes offline, compilação BibTeX e upload do PDF/log/resultados. Cada PDF de CI identifica o SHA compilado. As ligações às execuções verificadas serão registadas abaixo e no draft PR quando terminarem; não se atribui sucesso a uma execução ainda em curso.

## Questões para validação humana

| Prioridade | Decisão ou verificação | Estado |
|---|---|---|
| Antes de publicação | Confirmar voz, títulos, intensidade do humor e nota de assistência de IA. | Autor |
| Antes de publicação | Revalidar secção jurídica no texto consolidado em vigor e confirmar âmbito e calendário aplicáveis. Houve barreira anti-robot no acesso direto ao EUR-Lex. | Revisão jurídica/documental |
| Antes de publicação | Fazer leitura com pelo menos um principiante e um leitor técnico; identificar saltos, repetições e ambiguidades remanescentes. | Revisão de leitores |
| Antes de afirmar eficácia de um modelo | Executar labs selecionados com modelo/versionamento identificados, guardar saídas e avaliar casos novos. | Não executado nesta revisão |
| Antes de implementar MCP | Escolher SDK/versão e testar transporte, descoberta e autenticação. O exemplo implementa apenas o executor de domínio. | Extensão fora da demonstração offline |
| Antes de produção | Trocar papéis fictícios por autenticação real, dados protegidos, fila humana e operação com limites. | Demonstração não é serviço de produção |
| Aprovação editorial | Aceitar ou rever a estrutura e fazer merge apenas por decisão explícita do autor. | Draft PR, sem merge |

Os limites acima não invalidam os testes que foram executados. Delimitam o que esses testes demonstram e o que exigiria outra evidência.
