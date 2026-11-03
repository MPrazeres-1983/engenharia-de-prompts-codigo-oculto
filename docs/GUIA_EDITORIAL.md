# Guia editorial — Engenharia de Prompts: O Código Oculto

Português europeu, tratamento por «tu», ortografia consistente e tom direto. Conservar humor quando ajuda a lembrar o conceito; não usar uma piada como demonstração científica. A autoria permanece de Mário Prazeres. A assistência editorial deve ser declarada na nota de edição para revisão do autor.

## Explicação e evidência

Introduzir uma dificuldade concreta antes da abstração, definir o termo na primeira ocorrência e oferecer um exemplo verificável. Nem todas as secções precisam da mesma estrutura. Parágrafos curtos e listas quando ajudam a comparar; evitar transformar o livro numa coleção de caixas.

Distinguir explicitamente: **definição/facto estabelecido**, **resultado experimental** (modelo, tarefa, condições e alcance), **boa prática** (recomendação de engenharia), **hipótese/cenário**. As analogias descrevem uma intuição, não revelam o mecanismo de uma rede. Não inferir atenção interna a partir de duas respostas.

Usar citações junto das afirmações técnicas importantes. Preferir artigo original, livro de referência, documentação oficial versionada ou legislação consolidada. Uma página de marketing descreve o fornecedor, não constitui demonstração independente. Fixar versões de protocolo, data de consulta e limites de generalização. Não substituir referências verificadas por títulos inventados pelo modelo.

## Termos e exemplos

- «Treino», «inferência», «aprendizagem», «pesquisa», «registar», «controlos», «ficheiro», «equipa» e «utilizador».
- Manter identificadores de código e nomes oficiais em inglês. Explicar RAG, MCP, ETL e LLMOps ao introduzi-los.
- Um prompt condiciona o modelo; não garante execução como um programa. Persona não concede competência; confiança verbal não é calibração.
- JSON válido contém valores concretos. Opções e tipos pertencem a JSON Schema ou a uma tabela de campos; nunca usar `true/false` como valor JSON.
- Resultados ilustrativos são identificados; nenhum benchmark ou desempenho é inventado.

## Laboratórios

Cada Prompt Lab tem objetivo, contexto/material, procedimento, resultado esperado, validação e falhas possíveis. Nos comparativos, manter a entrada e as condições fixas, mudar uma variável e usar sessões separadas quando necessário. Distinguir desenvolvimento do teste reservado. Não prometer uma saída verbal específica de um modelo estocástico.

## Caso transversal

**A Lavandaria das Meias Desaparecidas** é inteiramente fictícia. A suspeita de que desaparecem só meias esquerdas é a premissa humorística da empresa, não um facto físico. IDs `LAV-001`, documentos `POL-01`/`POL-02`, utilizadores `cliente-A`/`cliente-B` e ferramentas têm definições no exemplo executável. O sistema consulta estado e prepara respostas; não aprova indemnizações nem envia mensagens automaticamente. Pesquisa lexical não deve ser apresentada como pesquisa vetorial; o adaptador de geração local não é um LLM.

## LaTeX

Entrada em `src/livro.tex`; capítulos em `src/capitulos`; preâmbulo separado. Labels sem números de capítulo, por exemplo `ch:rag`. Referências com `\ref`/`\cref`; bibliografia em `src/referencias.bib`, processada por BibTeX. Diagramas em TikZ, legíveis a 100% e com legendas. Não usar imagens geradas para informação técnica exata. Preservar a capa original.

## Revisão

Revisão automática: referências, citações, sintaxe dos exemplos, testes offline e logs. Revisão visual: capa, índice, páginas de capítulo, matemática, listagens, caixas, tabelas e figuras. Revisão humana: voz do autor, clareza para um principiante, adequação das interpretações científicas e jurídicas antes de publicação.
