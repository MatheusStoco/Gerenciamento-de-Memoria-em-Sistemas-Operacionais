# Gerenciamento-de-Memoria-em-Sistemas-Operacionais
Trabalho de alunos da UniCesumar, campus Curitiba/PR.

Curso: Engenharia de Software
Disciplina: Sistemas Operacionais
Professor: José Carlos Domingues Flores.

Objetivo:
Este trabalho tem como objetivo avaliar sua compreensão sobre os conceitos de gerenciamento
de memória em sistemas operacionais e sua capacidade de aplicar esses conceitos através da
implementação de códigos. O trabalho é composto por questões teóricas e práticas que exigem a
elaboração de programas preferencialmente nas linguagens C, Python ou Java.


Alocação de Memória em C: Estática (Pilha) vs. Dinâmica (Heap)

Este repositório contém um exemplo prático em C (alocação.c) que demonstra a diferença fundamental entre a alocação de memória estática (Stack - Pilha) e a alocação de memória dinâmica (Heap - Montante).
O código cria dois arrays e exibe seus endereços de memória para ilustrar que eles residem em regiões distintas da RAM. 

Conceito, Tipo de Alocação, Função/Localização, Características:
Estática: Array estatico[5], PILHA (Stack), "Tamanho fixo, alocado em tempo de compilação, liberação automática."

Dinâmica: Array *dinamico, HEAP (Montante),"Tamanho definido em tempo de execução (malloc), liberação manual (free)."

Como Compilar e Executar:

Para rodar este programa, você precisará de um compilador C (como o GCC) instalado em seu sistema operacional.

1. Compilação
Abra o terminal e use o GCC para compilar o arquivo alocação.c.

# O comando abaixo cria um arquivo executável chamado 'alocacao'
gcc alocação.c -o alocacao

2. Execução
Execute o arquivo gerado:
Sistema Operacional e Comando de Execução
Linux / macOS:   ./alocacao
Windows (Prompt/PowerShell):  .\alocacao

Análise da Saída
O resultado do programa demonstrará que:

1. Os endereços de memória dos elementos do array estático (Pilha) são próximos uns dos outros.

2. Os endereços de memória dos elementos do array dinâmico (Heap) também são sequenciais, mas a região da Heap está tipicamente muito distante da região da Pilha.

3. O programa finaliza com a mensagem de que a memória dinâmica foi liberada (free), um passo essencial para evitar vazamentos de memória (memory leaks)

