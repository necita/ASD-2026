\---

name: fechar-pr

description: Executa as etapas finais de uma alteração já implementada, verificando testes, documentação e preparação do PR.

metadata:

&#x20; intencao: executiva

&#x20; interacao: reativa

\---



\# Fechar PR



Esta skill deve ser usada quando uma alteração já foi implementada e precisa ser validada e preparada para entrega.



\## Objetivo



Executar as etapas finais sem interromper o fluxo com perguntas desnecessárias.



\## Procedimento



Ao ser acionada:



1\. Verifique o estado do repositório.

2\. Execute os testes automatizados disponíveis.

3\. Se os testes falharem, informe a falha e não considere a tarefa concluída.

4\. Verifique se a documentação necessária está atualizada.

5\. Faça as correções necessárias na documentação.

6\. Verifique novamente os testes.

7\. Revise as alterações realizadas.

8\. Prepare o conteúdo necessário para o Pull Request.



Durante a execução, não peça confirmação para cada etapa.



Se houver uma decisão que exija informação que não esteja disponível no projeto, informe claramente o bloqueio em vez de inventar uma resposta.



\## Critério de pronto



A execução estará concluída quando:



\- os testes relevantes passarem;

\- a documentação estiver atualizada;

\- as alterações estiverem revisadas;

\- o conteúdo do Pull Request estiver preparado.



Ao terminar, apresente um resumo contendo:



\- testes executados e resultado;

\- documentação atualizada;

\- arquivos alterados;

\- situação do Pull Request.

