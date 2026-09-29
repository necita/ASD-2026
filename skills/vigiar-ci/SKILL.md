\---

name: vigiar-ci

description: Analisa falhas de integração contínua e identifica a provável causa quando uma execução do CI falha.

metadata:

&#x20; intencao: assistiva

&#x20; interacao: autonoma

\---



\# Vigiar CI



Esta skill deve ser usada quando uma execução de integração contínua falhar.



\## Objetivo



Analisar automaticamente uma falha do CI e produzir um diagnóstico inicial sem depender de uma nova confirmação do usuário.



\## Procedimento



Quando uma falha do CI for detectada:



1\. Identifique qual etapa do CI falhou.

2\. Leia a mensagem de erro e os logs disponíveis.

3\. Relacione a falha com os arquivos e alterações recentes do projeto.

4\. Identifique a causa provável da falha.

5\. Indique quais arquivos ou componentes provavelmente precisam ser corrigidos.

6\. Registre um comentário ou relatório com:

&#x20;  - etapa que falhou;

&#x20;  - erro observado;

&#x20;  - causa provável;

&#x20;  - evidências encontradas;

&#x20;  - possível correção.



Não altere o código automaticamente nesta etapa.



Não invente informações que não estejam disponíveis nos logs ou no projeto.



\## Critério de pronto



A execução estará concluída quando houver um diagnóstico contendo:



\- a etapa que falhou;

\- o erro identificado;

\- a causa provável;

\- as evidências que sustentam o diagnóstico;

\- a indicação do próximo passo.



A skill deve executar essa análise de forma autônoma quando a falha do CI for detectada.

