# Questão 2 - Simulação de Fragmentação de Memória
# Autor: Matheus Stoco

# Criação das partições fixas da memória
memoria = [
    {"id": 1, "tamanho": 100, "processo": None, "tam_processo": 0},
    {"id": 2, "tamanho": 150, "processo": None, "tam_processo": 0},
    {"id": 3, "tamanho": 200, "processo": None, "tam_processo": 0},
    {"id": 4, "tamanho": 250, "processo": None, "tam_processo": 0},
    {"id": 5, "tamanho": 300, "processo": None, "tam_processo": 0}
]

# Função para alocar processo (First-Fit)
def alocar_processo(nome, tamanho):
    for p in memoria:
        if p["processo"] is None and p["tamanho"] >= tamanho:
            p["processo"] = nome
            p["tam_processo"] = tamanho
            frag = p["tamanho"] - tamanho
            print(f"Processo {nome} alocado na partição {p['id']} ({p['tamanho']} unidades).")
            print(f"Fragmentação interna: {frag} unidades.\n")
            return
    print(f"Não há partição disponível para o processo {nome} ({tamanho} unidades).\n")

# Função para liberar partição
def liberar_processo(nome):
    for p in memoria:
        if p["processo"] == nome:
            p["processo"] = None
            p["tam_processo"] = 0
            print(f"Processo {nome} liberado da partição {p['id']}.\n")
            return
    print(f"Processo {nome} não encontrado.\n")

# Função para exibir o estado da memória
def exibir_memoria():
    print("=== Estado atual da memória ===")
    for p in memoria:
        status = p["processo"] if p["processo"] else "Livre"
        print(f"Partição {p['id']}: {p['tamanho']} unidades - {status}")
    print("================================\n")

# Função para calcular a fragmentação total
def fragmentacao_total():
    total = 0
    for p in memoria:
        if p["processo"]:
            total += p["tamanho"] - p["tam_processo"]
    print(f"Fragmentação interna total: {total} unidades.\n")

# Teste do programa
if __name__ == "__main__":
    alocar_processo("P1", 90)
    alocar_processo("P2", 140)
    alocar_processo("P3", 180)
    liberar_processo("P2")
    alocar_processo("P4", 100)
    alocar_processo("P5", 350)  # Deve falhar
    exibir_memoria()
    fragmentacao_total()
