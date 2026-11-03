# Validação e fecho da segunda edição

Data: **3 de novembro de 2026**. O autor pediu expressamente para terminar as pendências e fazer merge do [PR #1](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/1). O trabalho continua na branch existente `segunda-edicao-2026`. A primeira edição fica preservada no histórico em `f63d417fb655c6af013569c5381235625e0567d1`; o merge não cria tag nem release.

## O que foi concluído

| Área | Evidência e resultado |
|---|---|
| Manuscrito | 29 capítulos, sete partes, três apêndices, 47 laboratórios e 41 entradas bibliográficas. Capa e licença originais preservadas. |
| Código offline | 30 testes passaram; 12/12 regressões conhecidas; `compileall` passou. Autorização, contratos e excertos verificados fora do modelo. |
| Inferência real | 52 chamadas locais com Qwen2.5-0.5B-Instruct Q4_K_M e llama.cpp b11960; 13 casos, duas variantes, duas seeds. Sem erros de execução; resultados negativos conservados. |
| Integridade do ensaio | Hashes do modelo/runtime/executor/saídas registados. O verificador reavalia as métricas a partir das respostas brutas sem nova inferência. |
| Ciência | Métodos originais de CoT, self-consistency, ToT e autocorreção consultados nas secções indicadas no registo de fontes. Não se afirma reprodução dos estudos ou leitura integral de todos os artigos. |
| Legislação | Afirmações do capítulo 28 confrontadas com disposições oficiais indexadas do RGPD, AI Act consolidado e Regulamento (UE) 2026/1744. Localizadores e limites de acesso registados. |
| Percurso inicial | Revistos capítulos 1–5: termos antes do uso, exemplo sem programação, critérios de resposta e ligação aos capítulos seguintes. Corrigida a inconsistência que tornava persona obrigatória. |
| Percurso técnico | Revistas as ligações entre fundamentos, raciocínio, contratos, Spec-First, MCP, demonstração e avaliação. Corrigidas imprecisões sobre embeddings e acrescentado o contraexemplo real de resposta falsa com citação válida. |

As duas leituras editoriais foram feitas pelo assistente na edição. **Não são um estudo com um principiante e um técnico humanos independentes.** O pedido de merge autoriza a integração do trabalho; não transforma esta revisão em evidência de um ensaio com leitores.

## Resultados do modelo: execução concluída não é tarefa resolvida

| Experiência | Resultado observado |
|---|---|
| Classificação por etiqueta exata | Zero-shot 6/12; few-shot 11/12. |
| Pedidos documentais, apenas prompt | JSON válido 6/6; contrato e proveniência 0/6. |
| Pedidos documentais, esquema no runtime | JSON válido 6/6; contrato e proveniência 1/6. |
| Duração em minutos | Pedido direto 1/8; instrução de decomposição 0/8. |

O único objeto documental que passou o contrato afirma «48 horas», contra a política citada. Nenhuma das 12 respostas documentais cumpre todos os critérios funcionais. É uma limitação demonstrada do modelo e da validação semântica, descrita no livro; não é ocultada para fazer parecer que o sistema está pronto para clientes. O funcionamento principal continua a usar templates offline. A amostra é sintética, pequena e não representa modelos de 2026 nem valida os 47 laboratórios.

[Procedimento, manifesto, saídas e revisão semântica](../experiencias/llm_local/README.md).

## Verificação jurídica documental

- RGPD: considerando 26; artigos 5, 6, 9, 22 e 35. Refinado o âmbito das decisões exclusivamente automatizadas e das salvaguardas nas exceções do artigo 22.
- AI Act: artigo 113, com alteração pelo artigo 1, ponto 40, do Regulamento (UE) 2026/1744; entrada em vigor deste pelo artigo 4. Confirmados os dois marcos de alto risco e os respetivos âmbitos.
- O acesso direto ao EUR-Lex continuou limitado por verificação anti-robot. As disposições relevantes foram obtidas da indexação do próprio texto oficial, incluindo o ato modificador e a consolidação de 27-07-2026. A limitação de acesso integral fica registada; as datas já não dependem apenas de uma cronologia institucional.
- Não houve parecer de advogado nem certificação de conformidade de um produto. O capítulo é enquadramento educativo e explicita a dependência da finalidade, papel, dados e regras aplicáveis.

## Compilação, PDF e CI

A primeira passagem desta revisão compilou em 198 páginas localmente (TeX Live 2023) e 199 na CI (TeX Live 2026), sem avisos relevantes. A execução [41666168658](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41666168658) documenta esse estado anterior, commit `5279d84f6e60d0cbc2d8f1d437fbda4db4ba4236`; não é apresentada como compilação das alterações de fecho.

A compilação de fecho local produziu 200 páginas, sem erros, citações/referências indefinidas ou avisos de composição detetados pelo verificador. A dependência portuguesa ausente no ambiente inicial foi reposta e a compilação repetida com sucesso. Inspecionadas as páginas alteradas de fundamentos, resultados, governação e bibliografia, além de capa, rosto e índice. Nenhum bloco de texto ficou fora da página. O merge exige CI bem-sucedida no commit final e inspeção do PDF dessa execução. O PR regista o SHA, as execuções finais e a decisão de merge. Cada artefacto da CI identifica o SHA realmente compilado e inclui PDF, log, resultados offline e registos das inferências.

Comandos, na raiz:

```bash
python3 -m unittest discover -s tests -v
python3 -m exemplos.lavandaria.avaliar
python3 experiencias/llm_local/verificar_registo.py
python3 -m compileall -q exemplos scripts tests experiencias
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error src/livro.tex
python3 scripts/verificar_livro.py --log src/livro.log
```

O validador de contrato é específico desta demonstração, não um motor genérico de JSON Schema nem um verificador de toda a semântica.

## Limites que permanecem declarados

| Atividade | Estado e consequência |
|---|---|
| Leitura com leitores independentes | Não realizada. Pode orientar uma revisão editorial posterior; não se inventa uma aprovação desses leitores. |
| Parecer jurídico profissional | Não realizado. Necessário decidir o seu alcance num caso concreto; não é substituído pela revisão documental. |
| Implementação de servidor MCP | Fora da demonstração. O livro explica o protocolo e testa o executor, sem alegar compatibilidade de servidor. |
| Serviço para clientes reais | Fora do âmbito: faltam autenticação real, avaliação representativa, operação e procedimentos humanos. Os ensaios observados não autorizam esse uso. |
| Publicação por tag/release | Não solicitada neste fecho. O pedido atual autoriza terminar e integrar o PR. |

A aprovação expressa do autor resolve a decisão de integração. As atividades externas não realizadas ficam distinguidas das verificações efetivamente executadas.
