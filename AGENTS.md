\# Instruções do projeto



\## Objetivo



Este projeto implementa um agente simples usando

Python e Ollama.



\## Arquivos principais



\- `agente.py`: implementação atual do agente e das ferramentas.

\- `diario/`: registros das atividades da disciplina.



\## Regras



\- Usar Python.

\- Usar Ollama para comunicação com o modelo.

\- Manter as ferramentas `consultar\_horario` e `consultar\_sala`.

\- Não remover funcionalidades existentes sem justificativa.

\- O limite de execução do agente deve ser controlado por `MAX\_PASSOS`.

\- O código deve ser testável sem depender de uma chamada real ao Ollama.

\- Alterações devem ser acompanhadas de testes quando aplicável.



\## Critério de pronto



A tarefa estará concluída quando:



1\. O agente possuir uma estrutura separada para execução das ferramentas.

2\. O limite de passos for respeitado.

3\. Erros de ferramenta ou argumentos forem tratados.

4\. As ferramentas existentes continuarem funcionando.

5\. Houver testes automatizados para a lógica principal.

6\. Os testes puderem ser executados sem Ollama.

7\. A documentação de execução estiver atualizada.

8\. O comportamento existente não for quebrado.

