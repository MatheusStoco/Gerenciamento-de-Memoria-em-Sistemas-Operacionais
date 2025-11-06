#include <stdio.h>  // Para printf rodar
#include <stdlib.h> // Para malloc, free, NULL, exit, EXIT_FAILURE rodar
#include <time.h>   // Para clock(), clock_t, CLOCKS_PER_SEC rodar 

// --- Constantes Configuraveis ---
#define NUM_ALLOCS 1000000 // // Define 1 milhao como o numero de alocacoes que faremos por teste
#define NUM_RUNS 50        // Define 50 como numero de rodadas dos testes para uma media razoável

// --- Prototipos das Funcoes ---
void funcao_pilha_auxiliar(void); // Função que permite a alocação e desaloca
void teste_pilha(void);  
void teste_heap(void);

// --- Funcoes de Teste ---

void funcao_pilha_auxiliar(void) {
    int variavel_local = 1; // aqui a memória é instantaneamente alocada no topo da pilha.
    if (variavel_local == 0) { // Apenas "usa" a variavel para que o compilador nao a otimize e remova
    }
} // Ao chegar nesta chave '}', a funcao termina. Toda a memoria alocada por ela (variavel_local) é
  // instantaneamente desalocada da pilha

  // Testeando a alocação na pilha (stack)
void teste_pilha(void) {
    for (long i = 0; i < NUM_ALLOCS; i++) { // Loop principal do teste de pilha
                                            // Repete o numero de vezes definido em NUM_ALLOCS (1 milhao)
        funcao_pilha_auxiliar(); //Chama a função auxiliar
    }
}

  // Testando a alocação no heap 
void teste_heap(void) {
    for (long i = 0; i < NUM_ALLOCS; i++) {
        int* ptr = (int*)malloc(sizeof(int));  // Pede manualmente ao sistema por um bloco de memoria do tamanho de um 'int'
                                               // O ponteiro 'ptr' guarda o endereco do bloco no heap
        if (ptr == NULL) {     // Verificacao de seguranca (boa pratica)
                            // Se 'malloc' falhar (ex: sem memoria), ptr sera NULL
            fprintf(stderr, "Falha na alocacao de memoria (heap) na iteracao %ld\n", i);
            exit(EXIT_FAILURE); 
        }
        *ptr = 1; // "Usa" a memoria alocada no heap
        free(ptr); // DESALOCACAO NO HEAP: devolve manualmente o bloco de memoria para o sistema.
                
    }
}

// --- Funcao Principal, onde o programada começa
int main(void) {
    clock_t inicio, fim; // Variaveis para marcar o tempo de inicio e fim de cada teste
    
    // Variaveis para somar o tempo total de todas as 50 rodadas
    double tempo_total_pilha = 0.0;
    double tempo_total_heap = 0.0;

    // Imprime o cabecalho do programa
    printf("===============================================================\n");
    printf("  Comparador de Desempenho de Alocacao de Memoria (Stack vs Heap)\n");
    printf("===============================================================\n");
    printf("Configuracao:\n");
    // Mostra os parametros do teste
    printf("  - Numero de alocacoes/desalocacoes por teste: %ld\n", (long)NUM_ALLOCS);
    printf("  - Numero de execucoes para media: %d\n", NUM_RUNS);
    printf("\nIniciando testes (isso pode levar alguns segundos)...\n");

    // Loop principal para repeticao (tira a media de NUM_RUNS rodadas)
    for (int i = 0; i < NUM_RUNS; i++) {
        printf("  Executando rodada %d/%d...\n", i + 1, NUM_RUNS);

        // --- Teste de Pilha (Stack) ---
        inicio = clock(); // Inicia o cronômetro
        teste_pilha(); // Roda o teste da pilha (1 milhao de alocacoes/desalocacoes)
        fim = clock(); // Para o cronometro
        tempo_total_pilha += ((double)(fim - inicio)) / CLOCKS_PER_SEC; // Calcula o tempo gasto (em segundos) e soma ao total da pilha

        // --- Teste de Heap ---
        inicio = clock(); // Inicia o cronometro novamente
        teste_heap(); // Roda o teste do heap (1 milhao de alocacoes/desalocacoes)
        fim = clock(); // Para o cronometro
        tempo_total_heap += ((double)(fim - inicio)) / CLOCKS_PER_SEC; // Calcula o tempo gasto (em segundos) e soma ao total do heap
    }

    // Avisa que todos os testes (todas as 50 rodadas) terminaram
    printf("...Testes concluidos.\n\n");

    // --- Calculo das Medias ---
    double media_pilha = tempo_total_pilha / NUM_RUNS;
    double media_heap = tempo_total_heap / NUM_RUNS;

    // Imprime a secao de resultados
    printf("===============================================================\n");
    printf("  Resultados Finais (Media de %d execucoes)\n", NUM_RUNS);
    printf("===============================================================\n");
    printf("  [Pilha (Stack)]\n"); // Mostra os resultados da Pilha
    printf("  Tempo medio total: %.6f segundos\n", media_pilha);
    printf("  Tempo medio por alocacao: ~%.10f segundos\n", media_pilha / NUM_ALLOCS);
    printf("\n");
    printf("  [Heap]\n"); // Mostra os resultados do Heap
    printf("  Tempo medio total: %.6f segundos\n", media_heap);
    printf("  Tempo medio por alocacao: ~%.10f segundos\n", media_heap / NUM_ALLOCS);
    printf("\n");

    // Imprime a secao de analise
    printf("---------------------------------------------------------------\n");
    printf("  Analise de Desempenho\n");
    printf("---------------------------------------------------------------\n");

    if (media_pilha > 0.0) {
        // Calcula a diferenca percentual
        double diferenca_percentual = ((media_heap - media_pilha) / media_pilha) * 100.0;
        // Imprime o resultado da comparacao
        printf("  -> A alocacao no HEAP foi %.2f%% mais lenta que na PILHA.\n", diferenca_percentual);
        printf("  -> A alocacao no HEAP foi %.2f vezes mais lenta que na PILHA.\n", media_heap / media_pilha);
    } else {
        // Caso a pilha seja rapida demais, apenas informa
        printf("  -> O tempo da Pilha foi rapido demais para ser medido com precisao (ou zero).\n");
    }
    printf("\n");
    printf("===============================================================\n");
    
    // Termina o programa e informa ao sistema que foi um sucesso (retorno 0)
    return 0; 
}