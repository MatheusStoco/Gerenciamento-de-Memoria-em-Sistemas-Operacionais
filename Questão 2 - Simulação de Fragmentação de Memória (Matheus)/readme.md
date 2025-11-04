# Questão 2 - Fragmentação de Memória

## Parte A - Teórica

- Fragmentação externa: ocorre quando há espaços livres na memória, mas eles estão divididos em blocos pequenos e separados, não sendo possível alocar um processo maior mesmo havendo espaço total suficiente.
- Fragmentação interna: ocorre quando um processo é colocado em uma partição maior do que o necessário, desperdiçando espaço dentro da partição.

Exemplos:

- Fragmentação externa: blocos livres de 50, 70 e 80, e um processo de 150 não cabe.
- Fragmentação interna: processo de 150 colocado em uma partição de 200 (sobra 50).

---

## Parte B - Programa em Python

- O programa simula um gerenciador de memória com partições fixas.
- Usa o método First-Fit (primeira partição livre que comporta o processo).
- Mostra a fragmentação interna e o estado atual da memória.

---

## Instruções para executar

1. Instalar o Python

   - Baixar e instalar em https://www.python.org/downloads
   - Durante a instalação, marcar a opção "Add Python to PATH"

2. Baixar ou clonar o repositório

   - Exemplo:
     ```bash
     git clone <url-do-repositorio>
     ```

3. Abrir o projeto no VS Code

4. Abrir o terminal no VS Code

   - Menu superior: Terminal → Novo Terminal

5. Entrar na pasta da questão

   ```bash
   cd "Questão 2 - Simulação de Fragmentação de Memória (Matheus)"

   ```

6. Executar o programa

   python questao2.py

7. O terminal mostrará as alocações, liberações e o total de fragmentação.

## Sequência de Teste

Alocar P1 (90)

Alocar P2 (140)

Alocar P3 (180)

Liberar P2

Alocar P4 (100)

Tentar alocar P5 (350)

Mostrar memória e fragmentação total
