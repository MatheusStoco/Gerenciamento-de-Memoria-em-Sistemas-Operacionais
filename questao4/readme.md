# 1\. Demonstração do Garbage Collector em Python (Questão 4)

**Contexto:** Este script é uma demonstração prática para a disciplina de Sistemas Operacionais, focando em como o Python gerencia a memória, especificamente o mecanismo de Coleta de Lixo (Garbage Collector ou GC).

## 2\. Visão Geral da Demonstração

O objetivo deste script é ilustrar visualmente os dois principais mecanismos de gerenciamento de memória do Python e suas limitações:

1.  **Contagem de Referências (Cenário 1):** O mecanismo padrão do Python. Um objeto é destruído *imediatamente* quando sua contagem de referências chega a zero.
2.  **Referências Circulares (Cenário 2):** A falha da contagem de referências. Quando objetos referenciam um ao outro (ex: `A` aponta para `B` e `B` aponta para `A`), suas contagens de referência nunca chegam a zero, mesmo que sejam inacessíveis do resto do programa. Isso cria um "vazamento de memória".
3.  **Coletor Geracional (Cenário 3):** A solução do Python para o problema acima. Um "detetive" (`gc.collect()`) que roda periodicamente para encontrar essas "ilhas" de objetos inacessíveis e limpá-las da memória.

## 3\. Código-Fonte Completo (`questao4.py`)

Para executar esta demonstração, faça o download do código questao4.py.

## 4\. Pré-requisitos

  * Você precisa ter o **Python 3** instalado em seu computador.
  * Para verificar a instalação, abra um terminal e execute `python --version` ou `python3 --version`. A saída deve ser algo como `Python 3.x.x`.

## 5\. Instruções de Execução

1.  **Abra seu Terminal:**

      * **Windows:** Procure por "Prompt de Comando", "PowerShell" ou "Terminal".
      * **macOS/Linux:** Procure por "Terminal".

2.  **Navegue até a Pasta:** Use o comando `cd` (change directory) para entrar na pasta onde você salvou o arquivo `questao4.py`.

      * *Exemplo (Windows):* `cd C:\Users\Thiago\Documentos\Faculdade\SO`
      * *Exemplo (macOS/Linux):* `cd /home/thiago/Documentos/Faculdade/SO`

3.  **Execute o Script:** Digite o comando abaixo e pressione Enter.

    ```bash
    python questao4.py
    ```

    *(Se o comando acima não funcionar, tente usar `python3 questao4.py`)*

## 6\. Saída Esperada e Análise

Ao executar o script, você verá a seguinte saída no seu terminal. Ela é dividida em três cenários para análise.

*(Nota: Os IDs dos objetos, como `(id: 22...)`, serão diferentes a cada execução, pois representam endereços de memória únicos).*

```
Desativando o GC automático para a demonstração...

============================================================
=== CENÁRIO 1: Contagem de Referências (Destruição Automática) ===
============================================================
1. Criando 'obj_cenario_1'...
Objeto 'A (Cenário 1)' CRIADO. (id: 22...)
    Refs de 'A': 2 (Esperado: 1 + 1 da função = 2)

2. Criando 'ref_extra' para o mesmo objeto...
    Refs de 'A': 3 (Esperado: 2 + 1 da função = 3)

3. Removendo a 'ref_extra' (atribuindo None)...
    Refs de 'A': 2 (Esperado: 1 + 1 da função = 2)

4. Removendo a referência final 'obj_cenario_1'...
Objeto 'A (Cenário 1)' DESTRUÍDO. (id: 22...) ---

Final do Cenário 1. O Objeto 'A' já deve ter sido destruído.
```

**Análise do Cenário 1:** O objeto `'A'` é destruído *exatamente* no momento em que a última variável (`obj_cenario_1`) deixa de apontar para ele. Isso mostra a contagem de referências funcionando perfeitamente.

```
============================================================
=== CENÁRIO 2: Referências Circulares (Falha da Contagem) ===
============================================================
1. Criando 'obj_B' e 'obj_C'...
Objeto 'B (Ciclo)' CRIADO. (id: 22...)
Objeto 'C (Ciclo)' CRIADO. (id: 22...)

2. Criando o ciclo: B aponta para C, C aponta para B

3. Criando 'obj_D' com auto-referência...
Objeto 'D (Auto-Ciclo)' CRIADO. (id: 22...)
4. Criando o ciclo: D aponta para si mesmo

Refs de 'B' (antes de deletar): 2
Refs de 'C' (antes de deletar): 2
Refs de 'D' (antes de deletar): 2

5. Removendo TODAS as referências externas (variáveis)...

!!! ATENÇÃO: NENHUMA MENSAGEM DE 'DESTRUÍDO' APARECEU !!!
    Os objetos B, C e D ainda estão na memória.
    Eles estão inacessíveis (nenhuma variável externa os alcança).
    Mas suas contagens de referência são 1, então o mecanismo padrão FALHOU.
    Isso é um 'vazamento de memória' (memory leak) temporário.
```

**Análise do Cenário 2:** Este é o ponto crucial. Mesmo após remover as variáveis `obj_B`, `obj_C` e `obj_D`, as mensagens `DESTRUÍDO` *não* aparecem. Isso ocorre porque:

  * `B` ainda é referenciado por `C`.
  * `C` ainda é referenciado por `B`.
  * `D` ainda é referenciado por si mesmo.
    A contagem de referências deles nunca chega a zero, e eles permanecem na memória.

<!-- end list -->

```
============================================================
=== CENÁRIO 3: Coletor Geracional (A Solução) ===
============================================================
O Coletor Geracional (gc) é o 'detetive' do Python.
Seu trabalho é rodar periodicamente para encontrar essas 'ilhas' de
objetos inacessíveis (ciclos) e limpá-los.

Forçando o 'detetive' a rodar agora com gc.collect()...
Objeto 'B (Ciclo)' DESTRUÍDO. (id: 22...) ---
Objeto 'C (Ciclo)' DESTRUÍDO. (id: 22...) ---
Objeto 'D (Auto-Ciclo)' DESTRUÍDO. (id: 22...) ---

Coleta concluída. Total de objetos inalcançáveis coletados: 3
Final do Cenário 3.

============================================================
=== ESTATÍSTICAS FINAIS DO GARBAGE COLLECTOR (gc.get_stats()) ===
============================================================
O GC mantém estatísticas sobre suas execuções.

Ger. 0 (Jovem): {'collections': ..., 'collected': 3, 'uncollectable': 0}
Ger. 1 (Média): {'collections': ..., 'collected': 0, 'uncollectable': 0}
Ger. 2 (Velha): {'collections': ..., 'collected': 0, 'uncollectable': 0}

Reativando o GC automático.
```

**Análise do Cenário 3:** Ao forçar a execução do coletor geracional (`gc.collect()`), ele analisa o grafo de objetos, identifica que `B`, `C` e `D` são inacessíveis (mesmo com referências internas) e os destrói, resolvendo o vazamento de memória. As estatísticas finais confirmam que 3 objetos foram coletados.
