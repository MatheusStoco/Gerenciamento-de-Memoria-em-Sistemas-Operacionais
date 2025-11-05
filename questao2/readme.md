# Questão 2 — Simulação de Fragmentação de Memória

## Descrição

Este projeto simula o processo de alocação de memória em partições fixas, demonstrando como ocorre a fragmentação interna durante a alocação de processos. A memória é organizada em blocos de tamanhos pré-definidos e utiliza o algoritmo First-Fit para escolher onde cada processo será alocado.

## Conceito de Fragmentação de Memória

A fragmentação é um efeito comum em sistemas operacionais durante a alocação e liberação de memória.

Fragmentação Externa:
Ocorre quando, apesar de existir memória livre total suficiente, ela está dividida em pequenos blocos não contíguos. Isso impede a alocação de processos maiores, pois não há um espaço contínuo que os comporte. Uma possível solução seria a compactação, porém isso é custoso e demanda processamento.

Fragmentação Interna:
Acontece quando o sistema utiliza partições de tamanho fixo. Se um processo ocupa uma partição maior do que o seu tamanho real, o espaço que sobra dentro dessa partição é desperdiçado — esse espaço desperdiçado é a fragmentação interna.

## Estrutura da Memória Simulada

A memória é composta por 5 partições fixas:

Partição 1: 100 unidades  
Partição 2: 150 unidades  
Partição 3: 200 unidades  
Partição 4: 250 unidades  
Partição 5: 300 unidades

Cada partição pode estar livre ou ocupada por um processo.

## Funcionalidades do Programa

alocar_processo(nome, tamanho):
Busca a primeira partição com espaço suficiente (First-Fit). Caso alocada, exibe a fragmentação interna gerada.

liberar_processo(nome):
Libera a partição ocupada pelo processo informado.

exibir_memoria():
Mostra o estado atual de todas as partições.

fragmentacao_total():
Calcula e exibe o total de fragmentação interna existente.

## Execução

Requisitos:

- Python instalado na máquina.

Como Executar:

1. Abra o terminal na pasta onde está o projeto:
   cd questao2

2. Execute o programa:
   python questao2.py

## Arquivo Principal

questao2.py — contém toda a lógica da simulação.
