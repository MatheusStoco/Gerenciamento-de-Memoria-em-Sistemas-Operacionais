# Questão 3 — Simulação do Algoritmo FIFO de Substituição de Página

## Descrição

Este projeto simula o algoritmo FIFO (First In First Out) de substituição de página, um mecanismo fundamental em sistemas de gerenciamento de memória virtual. O programa demonstra como páginas são carregadas em frames de memória e como o sistema decide qual página remover quando não há espaço disponível.

## Conceito de Substituição de Página FIFO

Em sistemas com memória virtual, quando o número de páginas referenciadas excede o número de frames (quadros) disponíveis, o sistema precisa decidir qual página remover da memória para fazer espaço para uma nova.

**Algoritmo FIFO (First In First Out):**
- Remove a página que foi carregada há mais tempo (a primeira a entrar)
- É simples de implementar, mas nem sempre é o mais eficiente
- Pode sofrer da anomalia de Bélády (aumentar frames pode aumentar page faults)

**Conceitos Importantes:**

- **Page Fault:** Quando uma página referenciada não está na memória, gerando uma interrupção
- **Page Hit:** Quando uma página referenciada já está na memória
- **Taxa de Falta de Página:** Proporção de page faults em relação ao total de referências
- **Frame:** Espaço de memória física que pode armazenar uma página

## Estrutura do Programa

O programa é composto pelos seguintes componentes:

### Classe `FIFOPageReplacement`

**Atributos:**
- `num_frames`: Número de frames disponíveis na memória
- `frames`: Lista que mantém as páginas carregadas em ordem FIFO
- `page_faults`: Contador de faltas de página
- `page_hits`: Contador de acertos
- `referencias`: Histórico de todas as referências processadas

**Métodos:**

- `__init__(num_frames)`: Inicializa o simulador
- `processar_referencia(pagina)`: Processa uma referência a uma página e retorna se houve page fault
- `simular(sequencia_paginas)`: Executa a simulação completa e exibe o resultado
- `_exibir_estatisticas()`: Calcula e exibe estatísticas finais

### Função `main()`

Controla a interação com o usuário:
1. Solicita o número de frames disponíveis
2. Solicita a sequência de referências a páginas
3. Executa a simulação
4. Oferece a opção de executar novamente

## Como Usar

### Execução do Programa

```bash
python atividade3.py
```

### Entrada de Dados

1. **Número de frames:** Digite um inteiro positivo representando a quantidade de frames
2. **Sequência de referências:** Digite os números de página separados por vírgula ou espaço
   - Exemplo: `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
   - Ou: `7 0 1 2 0 3 0 4 2 3 0 3 2`

### Saída Esperada

```
================================================================================
SIMULAÇÃO DO ALGORITMO FIFO DE SUBSTITUIÇÃO DE PÁGINA
================================================================================
Número de frames disponíveis: 3
Sequência de referências: [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
================================================================================

Referência:  7 | Frames: [7]                | Page Fault                          | Total Faults: 1
Referência:  0 | Frames: [7, 0]             | Page Fault                          | Total Faults: 2
Referência:  1 | Frames: [7, 0, 1]          | Page Fault                          | Total Faults: 3
Referência:  2 | Frames: [0, 1, 2]          | Page Fault (substituiu 7)           | Total Faults: 4
Referência:  0 | Frames: [0, 1, 2]          | Page Hit                            | Total Faults: 4
Referência:  3 | Frames: [1, 2, 3]          | Page Fault (substituiu 0)           | Total Faults: 5
Referência:  0 | Frames: [2, 3, 0]          | Page Fault (substituiu 1)           | Total Faults: 6
Referência:  4 | Frames: [3, 0, 4]          | Page Fault (substituiu 2)           | Total Faults: 7
Referência:  2 | Frames: [0, 4, 2]          | Page Fault (substituiu 3)           | Total Faults: 8
Referência:  3 | Frames: [4, 2, 3]          | Page Fault (substituiu 0)           | Total Faults: 9
Referência:  0 | Frames: [2, 3, 0]          | Page Fault (substituiu 4)           | Total Faults: 10
Referência:  3 | Frames: [2, 3, 0]          | Page Hit                            | Total Faults: 10
Referência:  2 | Frames: [2, 3, 0]          | Page Hit                            | Total Faults: 10

================================================================================
ESTATÍSTICAS FINAIS
================================================================================
Total de referências: 13
Page Faults (faltas de página): 10
Page Hits (acertos): 3
Taxa de falta de página: 76.92%
Taxa de acerto de página: 23.08%
================================================================================
```

## Funcionalidades

✅ Interface interativa com o usuário  
✅ Validação de entrada de dados  
✅ Simulação completa do algoritmo FIFO  
✅ Exibição do estado dos frames após cada referência  
✅ Identificação clara de page faults e page hits  
✅ Cálculo de estatísticas finais com taxas percentuais  
✅ Opção de executar múltiplas simulações  
✅ Sem dependências de bibliotecas externas  

## Estrutura de Dados Utilizada

O programa utiliza uma **lista (ArrayList)** para armazenar os frames, aproveitando sua natureza FIFO através das operações:
- `append()`: Adiciona novo elemento no final (página entra)
- `pop(0)`: Remove o primeiro elemento (página mais antiga sai)
- `in`: Verifica se uma página está presente

Essa estrutura simula perfeitamente o comportamento de uma fila FIFO.

## Exemplos de Uso

### Exemplo 1: Sequência Simples

```
Frames: 3
Sequência: 1 2 3 1 2 4

Resultado: 5 page faults de 6 referências
Taxa de falta: 83.33%
```

### Exemplo 2: Sequência com Repetição

```
Frames: 2
Sequência: 1 2 1 2 1 2

Resultado: 2 page faults de 6 referências
Taxa de falta: 33.33%
```

## Observações Importantes

1. O algoritmo FIFO não considera a frequência de uso das páginas
2. Pode não ser o algoritmo mais eficiente (suscetível à anomalia de Bélády)
3. É simples de implementar, mas algoritmos como LRU podem ser melhores
4. A complexidade é O(1) para processamento de cada referência com listas pequenas

## Autor

Lucas Vaz