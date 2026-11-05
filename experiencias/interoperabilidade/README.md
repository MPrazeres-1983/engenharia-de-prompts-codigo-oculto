# A consulta da receção ao arquivo

Ensaio executado em 5 de novembro de 2026, com Python 3.12.14. Usa dados fictícios e apenas a biblioteca padrão de Python 3.10 ou posterior. Da pasta principal do projeto, executa:

~~~bash
python3 -m experiencias.interoperabilidade.executar
~~~

A receção recebe uma mensagem sem número de reclamação. Cria uma tarefa e pede o número. Quando o recebe do mesmo cliente, chama o arquivo e devolve o resultado como artefacto da tarefa. Para acompanhar em papel, escreve a identidade, o número da tarefa, a mensagem e o estado depois de cada troca. Um pedido pode receber uma resposta HTTP 200 enquanto a tarefa ainda espera informação.

| Ligação | O que corre | Âmbito verificado |
|---|---|---|
| Cliente → receção | Pedidos HTTP à própria máquina, em endereço e porta locais | A2A 1.0.0 com versão de comunicação 1.0. Cartão, envio de mensagem, consulta e retoma da tarefa |
| Receção → arquivo | Mensagens JSON-RPC pela entrada e saída de outro processo Python | MCP 2026-07-28. Descoberta, listagem, chamada de uma ferramenta e erro de versão incompatível |
| Arquivo → dados | Executor da Lavandaria já usado no livro | Leitura autorizada, recusa de argumentos extra e mensagem igual para reclamação inacessível ou ausente |

As credenciais A e B são valores fictícios do ensaio. A receção valida a credencial e associa a tarefa ao cliente. Passa ao processo do arquivo a identidade que reconheceu, fora dos argumentos da ferramenta. O arquivo verifica a titularidade da reclamação. As tarefas ficam na memória durante o ensaio e o servidor termina no fim. A aplicação usa apenas ligações locais, zero chamadas a um LLM e leitura dos dados fictícios.

O [resultado registado](resultado-2026-11-05.json) contém as dez verificações. O comando falha se uma observação divergir do critério. Duas execuções deram o mesmo resumo. O ficheiro omite a porta local e os identificadores gerados em cada execução.

As duas implementações cobrem as operações do quadro. Um teste de conformidade teria de cobrir o restante protocolo e usar clientes ou servidores independentes. O armazenamento, a autenticação, o controlo de tráfego e a operação de produção têm requisitos próprios.

- [MCP 2026-07-28, transporte stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)
- [MCP, descoberta](https://modelcontextprotocol.io/specification/2026-07-28/server/discover) e [ferramentas](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [A2A 1.0.0, versões, tarefas e binding HTTP+JSON](https://a2a-protocol.org/v1.0.0/specification/)
