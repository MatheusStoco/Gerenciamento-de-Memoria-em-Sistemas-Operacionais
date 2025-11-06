#include <stdio.h>
#include <stdlib.h>

int main() {

    
    // 1. ARRAY ESTÁTICO
    
    // Aqui é criado um array "estatico" de tamanho fixo 5.
    // Esse tipo de array fica armazenado na memória de pilha (stack),
    // e seu tamanho precisa ser definido antes do programa rodar.
    int estatico[5];

    // Preenchendo o array com valores de 1 a 5.
    // O índice começa em 0, então "i + 1" deixa os valores de 1 a 5.
    for (int i = 0; i < 5; i++) {
        estatico[i] = i + 1;
    }

    
    // 2. ARRAY DINÂMICO
    
    // Diferente do estático, este array é criado em tempo de execução.
    // Para isso usamos malloc, que reserva um espaço na memória heap.
    // Aqui reservamos espaço para 10 inteiros.
    int *dinamico = (int *) malloc(10 * sizeof(int));

    // É sempre importante verificar se o malloc funcionou.
    // Caso não haja memória suficiente, malloc retorna NULL.
    if (dinamico == NULL) {
        printf("Erro: falha na alocacao de memoria.\n");
        return 1;
    }

    // Preenchendo o array dinâmico com valores de 10 a 19.
    for (int i = 0; i < 10; i++) {
        dinamico[i] = 10 + i;
    }

    
    // 3. EXIBINDO O ARRAY ESTÁTICO
    
    printf("=== ARRAY ESTATICO (PILHA) ===\n");
    for (int i = 0; i < 5; i++) {
        // &estatico[i] mostra o endereço daquele elemento na memória
        printf("Indice [%d] -> Valor: %2d | Endereco: %p\n", 
               i, estatico[i], (void*)&estatico[i]);
    }

   
    // 4. EXIBINDO O ARRAY DINÂMICO

    printf("\n=== ARRAY DINAMICO (HEAP) ===\n");
    for (int i = 0; i < 10; i++) {
        // Aqui usamos (dinamico + i) para mostrar o endereço do i-ésimo elemento
        printf("Indice [%d] -> Valor: %2d | Endereco: %p\n", 
               i, dinamico[i], (void*)(dinamico + i));
    }

   
    // 5. COMPARAÇÃO ENTRE ENDEREÇOS

    printf("\n=== DIFERENCA ENTRE ENDERECOS ===\n");
    // Endereço base do array estático
    printf("Endereco inicial do array estatico: %p\n", (void*)estatico);
    // Endereço base do array dinâmico
    printf("Endereco inicial do array dinamico: %p\n", (void*)dinamico);

    // Convertendo os endereços para char* para calcular a diferença em bytes
    long diferenca = (long)((char*)dinamico - (char*)estatico);
    printf("Diferenca entre os enderecos (em bytes): %ld\n", diferenca);

    printf("Observacao: array estatico -> armazenado na PILHA\n");
    printf("            array dinamico -> armazenado na HEAP\n");

   
    // 6. LIBERAÇÃO DA MEMÓRIA

    // Como o array dinâmico foi alocado com malloc,
    // precisamos liberar essa memória quando não for mais usada.
    free(dinamico);

    printf("\nMemoria dinamica liberada com sucesso.\n");

    return 0;
}
