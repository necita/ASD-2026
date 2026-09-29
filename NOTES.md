\# Notas de exploração



\## Estado atual



O projeto possui um agente Python que utiliza a biblioteca `ollama`

para realizar function calling.



O agente possui duas ferramentas:



\- `consultar\_horario()`, sem parâmetros.

\- `consultar\_sala(sala)`, que recebe o número da sala.



O código possui `MAX\_PASSOS = 5`.



\## Comportamento observado



Durante o primeiro experimento, o modelo escolheu corretamente

`consultar\_sala` para a pergunta sobre a sala 203.



A ferramenta recebeu `sala = 203` e retornou:



`Sala 203 - Segundo andar`.



A primeira versão do agente tentou executar um segundo passo após

a ferramenta e ficou aguardando uma nova resposta do Ollama.



Para o experimento anterior, o laço foi ajustado para finalizar

após a execução da ferramenta.



\## Problemas identificados



\- A lógica das ferramentas e a lógica do agente estão concentradas

&#x20; em um único arquivo.

\- A execução depende diretamente do Ollama.

\- A lógica principal não possui testes automatizados independentes.

\- O tratamento de erros é limitado.

\- O comportamento do loop precisa ser mais robusto.



\## Direção da refatoração



Separar ferramentas, execução do agente e testes, mantendo o

comportamento existente e tornando a lógica principal testável

sem depender do Ollama.

