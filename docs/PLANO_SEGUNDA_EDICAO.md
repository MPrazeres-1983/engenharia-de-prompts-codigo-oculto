# Plano e estrutura da segunda edição

Base preservada em `main@f63d417`; trabalho em `segunda-edicao-2026`. Sem merge, tag ou lançamento definitivo. Data de corte documental: **3 de novembro de 2026**.

## Sequência implementada

| Parte | Capítulos | Dependência pedagógica |
|---|---|---|
| I. Começar do zero | 1. IA, aprendizagem e modelos; 2. A primeira conversa; 3. Mentalidade; 4. Contexto e exemplos; 5. Personas e instruções | Não exige programação; introduz modelo, prompt, contexto, validação e primeira experiência. |
| II. Dentro da máquina | 6. Desligar a magia; 7. Transformer; 8. Tokens e amostragem; 9. Multimodalidade | Parte I antes da notação. Treino, inferência e vetores são explicados antes de atenção e raciocínio. |
| III. Raciocínio e verificação | 10. CoT, ToT e modelos de raciocínio; 11. Autocorreção e ferramentas | Amostragem e contexto antes de discutir diversidade, explicação e verificadores. |
| IV. Comunicação e aprendizagem | 12. Escrita; 13. Estudo; 14. Negócios; 15. Narrativa; 16. Investigação | Aplica prompts e validação a domínios; leitura possível por interesse. |
| V. Software e dados | 17. Texto→dados; 18. Análise; 19. Software com IA; 20. Spec-First | Introduz JSON e contratos antes da implementação e dos testes rastreáveis. |
| VI. Construir sistemas | 21. RAG; 22. Ferramentas e MCP; 23. Cadeias e agentes; 24. Lavandaria executável | Documentos e interfaces antes de orquestração. Caso final reúne as peças com limites explícitos. |
| VII. Avaliar, proteger e operar | 25. Avaliação; 26. Segurança; 27. LLMOps; 28. Governação; 29. Futuro | Arquitetura conhecida antes de avaliar e operar. Segurança mínima acompanha ferramentas desde o início. |
| Apêndices | A. Biblioteca de padrões; B. Glossário; C. Como ler as fontes; bibliografia | Consulta transversal e aprofundamento. |

Não é necessário ler álgebra antes da primeira experiência. Um leitor técnico pode começar nos capítulos 17–24, usando as referências cruzadas. A tabela é o índice editorial; o índice paginado é gerado pelo LaTeX.

## Método de execução

1. Auditoria integral com prioridades e registo da base.
2. Modularização sem perda de capítulos; revisão científica e lexical; reordenação.
3. Capítulos novos, fontes verificadas e diagramas TikZ.
4. Protocolo individual para todos os 39 laboratórios existentes e para os novos.
5. Caso offline com dados fictícios, contrato e testes independentes; interfaces de LLM descritas sem fabricar execuções.
6. Compilação, verificação de citações e referências, testes, inspeção visual e validação por Actions.
7. Commits por conjunto coerente; draft PR para revisão humana.

## Critérios de aceitação

- Capa original byte a byte; licença e autoria preservadas.
- Todos os capítulos originais mapeados na auditoria; cortes substanciais justificados no changelog.
- Nenhuma referência LaTeX/citação indefinida; nenhuma listagem cortada; fórmulas verificadas.
- Simulações, execuções determinísticas, estudos publicados e hipóteses separados no texto.
- Nenhuma chamada paga nem envio de dados reais necessário para executar a demonstração offline.
- Limitações técnicas e pontos de revisão humana explícitos. A compilação é necessária, mas não certifica a qualidade científica ou editorial.
