# Questão 3 - Simulação do Algoritmo FIFO de Substituição de Página
# Autor: Lucas Vaz

# ========================================================================
# BLOCO 1: DEFINIÇÃO E INICIALIZAÇÃO DA CLASSE FIFO
# ========================================================================
# Implementa o algoritmo FIFO (First In First Out) para simular
# substituição de páginas em memória virtual
class FIFOPageReplacement:
    
    def __init__(self, num_frames):
        # Armazena o número de frames disponíveis na memória
        self.num_frames = num_frames
        # Lista que mantém as páginas carregadas nos frames
        self.frames = []
        # Contadores para estatísticas de desempenho
        self.page_faults = 0
        self.page_hits = 0
        # Histórico de todas as referências processadas
        self.referencias = []
    
    def processar_referencia(self, pagina):
        # ========================================================================
        # BLOCO 2: PROCESSAMENTO DE REFERÊNCIAS E SUBSTITUIÇÃO FIFO
        # ========================================================================
        # Verifica se a página já está nos frames (Page Hit)
        if pagina in self.frames:
            self.page_hits += 1
            return False, None
        
        # Página não está na memória, incrementa contador de faltas
        self.page_faults += 1
        pagina_substituida = None
        
        # Se há espaço livre, simplesmente adiciona a página
        if len(self.frames) < self.num_frames:
            self.frames.append(pagina)
        else:
            # Frames cheios: remove a primeira página (mais antiga)
            # e adiciona a nova página (Algoritmo FIFO)
            pagina_substituida = self.frames.pop(0)
            self.frames.append(pagina)
        
        return True, pagina_substituida
    
    def simular(self, sequencia_paginas):
        # ========================================================================
        # BLOCO 3: SIMULAÇÃO E EXIBIÇÃO DOS RESULTADOS
        # ========================================================================
        # Exibe cabeçalho com informações iniciais da simulação
        print("=" * 80)
        print("SIMULAÇÃO DO ALGORITMO FIFO DE SUBSTITUIÇÃO DE PÁGINA")
        print("=" * 80)
        print(f"Número de frames disponíveis: {self.num_frames}")
        print(f"Sequência de referências: {sequencia_paginas}")
        print("=" * 80)
        print()
        
        # Armazena a sequência e processa cada referência de página
        self.referencias = sequencia_paginas
        
        for i, pagina in enumerate(sequencia_paginas):
            # Processa a referência e formata a saída de cada etapa
            eh_page_fault, pagina_substituida = self.processar_referencia(pagina)
            
            tipo_evento = "Page Hit" if not eh_page_fault else "Page Fault"
            
            if eh_page_fault and pagina_substituida is not None:
                tipo_evento += f" (substituiu {pagina_substituida})"
            
            total_eventos = self.page_faults + self.page_hits
            
            print(f"Referência: {pagina:2d} | Frames: {str(self.frames):20s} | "
                  f"{tipo_evento:35s} | Total Faults: {self.page_faults}")
        
        print()
        self._exibir_estatisticas()
    
    def _exibir_estatisticas(self):
        # ========================================================================
        # BLOCO 3 (CONTINUAÇÃO): CÁLCULO E EXIBIÇÃO DE ESTATÍSTICAS
        # ========================================================================
        # Calcula estatísticas de desempenho da simulação
        total_referencias = len(self.referencias)
        total_eventos = self.page_faults + self.page_hits
        taxa_falta = (self.page_faults / total_referencias * 100) if total_referencias > 0 else 0
        taxa_acerto = (self.page_hits / total_referencias * 100) if total_referencias > 0 else 0
        
        # Exibe os resultados finais e métricas de desempenho
        print("=" * 80)
        print("ESTATÍSTICAS FINAIS")
        print("=" * 80)
        print(f"Total de referências: {total_referencias}")
        print(f"Page Faults (faltas de página): {self.page_faults}")
        print(f"Page Hits (acertos): {self.page_hits}")
        print(f"Taxa de falta de página: {taxa_falta:.2f}%")
        print(f"Taxa de acerto de página: {taxa_acerto:.2f}%")
        print("=" * 80)


def main():
    
    # ========================================================================
    # BLOCO 4: ENTRADA DE DADOS DO USUÁRIO
    # ========================================================================
    # Interface interativa para obter número de frames
    print("\n>>> SIMULADOR FIFO DE SUBSTITUIÇÃO DE PÁGINA <<<\n")
    
    # Valida e obtém o número de frames (deve ser positivo)
    while True:
        try:
            num_frames = int(input("Digite o número de frames disponíveis: "))
            if num_frames <= 0:
                print("O número de frames deve ser maior que 0. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    
    # Solicita e valida a sequência de referências de páginas
    print("\nDigite a sequência de referências a páginas.")
    print("Separe os números por vírgula ou espaço.")
    print("Exemplo: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2")
    
    while True:
        try:
            entrada = input("Sequência de referências: ")
            # Tenta separar por vírgula primeiro, depois por espaço
            if ',' in entrada:
                sequencia = [int(x.strip()) for x in entrada.split(',')]
            else:
                sequencia = [int(x.strip()) for x in entrada.split()]
            
            if not sequencia:
                print("A sequência não pode estar vazia. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite números inteiros separados por vírgula ou espaço.")
    
    print()
    
    # ========================================================================
    # BLOCO 5: EXECUÇÃO DA SIMULAÇÃO E CONTROLE DE REPETIÇÃO
    # ========================================================================
    # Cria instância do simulador e executa com os dados fornecidos
    simulador = FIFOPageReplacement(num_frames)
    simulador.simular(sequencia)
    
    # Permite ao usuário executar nova simulação
    print()
    while True:
        novamente = input("Deseja executar novamente? (s/n): ").lower().strip()
        if novamente in ['s', 'n']:
            break
    
    # Se usuário desejar, chama main() recursivamente
    if novamente == 's':
        main()
    else:
        print("\nObrigado por usar o simulador FIFO!")


if __name__ == "__main__":
    main()
