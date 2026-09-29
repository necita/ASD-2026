---
name: planejar-pr
description: Planeja uma alteração de projeto antes da implementação, coletando escopo, arquivos afetados e critério de pronto.
metadata:
  intencao: assistiva
  interacao: interativa
---

# Planejar PR

Esta skill deve ser usada antes de iniciar uma alteração significativa no projeto.

## Objetivo

Ajudar a definir o escopo da alteração antes de qualquer código ser modificado.

## Procedimento

Antes de implementar qualquer alteração, pergunte ao usuário:

1. Qual é o objetivo da alteração?
2. Quais arquivos ou áreas do projeto podem ser afetados?
3. Qual comportamento existente deve ser preservado?
4. Qual é o critério de pronto?
5. Quais testes devem confirmar que a alteração foi concluída?

Não modifique arquivos durante esta etapa.

Depois das respostas, apresente um plano curto contendo:

- objetivo;
- arquivos provavelmente afetados;
- etapas de implementação;
- testes necessários;
- critério de pronto.

A implementação só deve começar depois que o usuário confirmar o plano.