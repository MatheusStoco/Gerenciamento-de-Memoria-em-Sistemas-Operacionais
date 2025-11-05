# Questão 2 - Simulação de Fragmentação de Memória (Matheus)

## Descrição

Este projeto simula a alocação de memória em partições fixas, demonstrando como ocorre fragmentação interna durante o processo de alocação. A memória é dividida em tamanhos predeterminados e os processos são alocados utilizando o algoritmo First-Fit.

## Conceito de Fragmentação de Memória

A fragmentação é um problema comum na alocação dinâmica de memória em sistemas operacionais. Conforme os blocos de memória são constantemente alocados e liberados, a memória pode se fragmentar, dificultando o uso eficiente do espaço disponível.

- Fragmentação Externa:
  Ocorre quando há memória livre total suficiente, porém ela está dividida em pequenos blocos separados. Mesmo existindo espaço livre no total, ele não está em um único bloco contíguo, impedindo a alocação de processos maiores. Uma possível solução é a compactação, que reorganiza os blocos livres, mas este processo é custoso e exige tempo de processamento.

- Fragmentação Interna:
  Acontece em sistemas que utilizam partições fixas. Quando um processo ocupa uma partição maior do que o necessário, o espaço restante dentro dessa partição é desperdiçado. Esse espaço sobrando é considerado fragmentação interna.

## Estrutura da Memória Simulada

A memória foi dividida em 5 partições fixas:

- Partição 1: 100 unidades
- Partição 2: 150 unidades
- Partição 3: 200 unidades
- Partição 4: 250 unidades
- Partição 5: 300 unidades

Cada partição pode estar livre ou ocupada por um processo.

## Funcionalidades do Programa

- `alocar_processo(nome, tamanho)`:
  Procura a primeira partição livre que comporte o processo (algoritmo First-Fit). Caso alocado, mostra a fragmentação interna da partição.

- `liberar_processo(nome)`:
  Libera a partição ocupada pelo processo informado.

- `exibir_memoria()`:
  Mostra o estado atual das partições (livres ou ocupadas).

- `fragmentacao_total()`:
  Calcula e exibe a soma total da fragmentação interna existente nas partições ocupadas.

## Execução

### Requisitos

- Python instalado

### Como executar

Abra o terminal na pasta do projeto:

cd questao2

Execute o programa:

python questao2.py

Se necessário, substitua por:

## Arquivo Principal

- `questao2.py` — contém toda a implementação da simulação.
