Questão 5: Comparador de Desempenho de Memória (Pilha vs. Heap)
Este é um programa em C desenvolvido para a Questão 5, com o objetivo de demonstrar e medir empiricamente a diferença de performance entre a alocação de memória na Pilha (Stack) e no Heap.

🧠 O que o programa faz?
O script mem_test.c executa dois testes de "estresse" para comparar os dois tipos de alocação de memória:

Teste de Pilha (Stack): Simula um grande número de alocações e desalocações chamando uma função auxiliar (funcao_pilha_auxiliar) repetidamente em um loop. A entrada na função força uma alocação (criação de variável local) e a saída da função força uma desalocação (destruição do escopo) de forma automática.

Teste de Heap: Simula o mesmo número de alocações e desalocações, mas de forma manual, chamando as funções malloc() (para alocar) e free() (para desalocar) explicitamente dentro de um loop.

Cálculo de Média: Para garantir um resultado confiável e remover anomalias, o programa executa ambos os testes um grande número de vezes (ex: 50 rodadas) e calcula o tempo médio de cada um.

Resultado: Ao final, o programa exibe o tempo médio total de cada teste e calcula a diferença percentual de desempenho, mostrando o quanto a alocação no Heap foi mais lenta que na Pilha.

🛠️ Configuração
O comportamento do teste pode ser ajustado alterando as seguintes constantes (#define) no topo do arquivo mem_test.c:

NUM_ALLOCS: Define o número de alocações/desalocações que serão feitas dentro de cada rodada.
Padrão: 1000000 (1 milhão)

NUM_RUNS: Define o número de rodadas de teste que serão executadas para o cálculo da média.
Padrão: 50

🚀 Instruções para Executar
Este programa foi compilado e testado em um ambiente macOS (Apple Clang / GCC).

> Navegue até a pasta: Abra seu terminal e certifique-se de que você está no diretório correto (provavelmente questao5).
> Compile o programa: Use o gcc (ou clang) para compilar o arquivo .c e gerar um arquivo executável.

Bash
gcc mem_test.c -o mem_test
gcc: O comando do compilador.
mem_test.c: O arquivo-fonte.

-o mem_test: O nome do arquivo executável de saída (output).

Execute o programa: Após a compilação, execute o programa recém-criado.

Bash
./mem_test
