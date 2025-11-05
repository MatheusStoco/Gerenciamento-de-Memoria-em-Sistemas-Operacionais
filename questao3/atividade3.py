# Questão 3 - Simulação do Algoritmo FIFO de Substituição de Página
# Autor: Matheus Stoco


class FIFOPageReplacement:
    """
    Simula o algoritmo FIFO (First In First Out) de substituição de página.
    Este algoritmo substitui a página mais antiga quando não há frames livres.
    """
    
    def __init__(self, num_frames):
        """
        Inicializa o simulador FIFO.
        
        Args:
            num_frames (int): Número de frames (quadros) disponíveis na memória
        """
        self.num_frames = num_frames
        self.frames = []  # Lista que armazena as páginas nos frames
        self.page_faults = 0
        self.page_hits = 0
        self.referencias = []  # Histórico de referências
    
    def processar_referencia(self, pagina):
        """
        Processa uma referência a uma página.
        
        Args:
            pagina (int): Número da página sendo referenciada
            
        Returns:
            tuple: (é_page_fault, página_substituída ou None)
        """
        # Verifica se a página já está nos frames (Page Hit)
        if pagina in self.frames:
            self.page_hits += 1
            return False, None
        
        # Page Fault: página não está nos frames
        self.page_faults += 1
        pagina_substituida = None
        
        # Se há frames livres, adiciona a página
        if len(self.frames) < self.num_frames:
            self.frames.append(pagina)
        else:
            # Não há frames livres: remove a primeira (FIFO) e adiciona a nova
            pagina_substituida = self.frames.pop(0)
            self.frames.append(pagina)
        
        return True, pagina_substituida
    
    def simular(self, sequencia_paginas):
        """
        Executa a simulação do algoritmo FIFO.
        
        Args:
            sequencia_paginas (list): Lista de números de página a referenciar
        """
        print("=" * 80)
        print("SIMULAÇÃO DO ALGORITMO FIFO DE SUBSTITUIÇÃO DE PÁGINA")
        print("=" * 80)
        print(f"Número de frames disponíveis: {self.num_frames}")
        print(f"Sequência de referências: {sequencia_paginas}")
        print("=" * 80)
        print()
        
        self.referencias = sequencia_paginas
        
        for i, pagina in enumerate(sequencia_paginas):
            eh_page_fault, pagina_substituida = self.processar_referencia(pagina)
            
            # Formata a saída
            tipo_evento = "Page Hit" if not eh_page_fault else "Page Fault"
            
            if eh_page_fault and pagina_substituida is not None:
                tipo_evento += f" (substituiu {pagina_substituida})"
            
            total_eventos = self.page_faults + self.page_hits
            
            print(f"Referência: {pagina:2d} | Frames: {str(self.frames):20s} | "
                  f"{tipo_evento:35s} | Total Faults: {self.page_faults}")
        
        print()
        self._exibir_estatisticas()
    
    def _exibir_estatisticas(self):
        """Exibe as estatísticas finais da simulação."""
        total_referencias = len(self.referencias)
        total_eventos = self.page_faults + self.page_hits
        taxa_falta = (self.page_faults / total_referencias * 100) if total_referencias > 0 else 0
        taxa_acerto = (self.page_hits / total_referencias * 100) if total_referencias > 0 else 0
        
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
    """Função principal que executa o programa."""
    
    # Entrada do usuário
    print("\n>>> SIMULADOR FIFO DE SUBSTITUIÇÃO DE PÁGINA <<<\n")
    
    # Solicita o número de frames
    while True:
        try:
            num_frames = int(input("Digite o número de frames disponíveis: "))
            if num_frames <= 0:
                print("O número de frames deve ser maior que 0. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    
    # Solicita a sequência de referências
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
    
    # Cria e executa o simulador
    simulador = FIFOPageReplacement(num_frames)
    simulador.simular(sequencia)
    
    # Opção de executar novamente
    print()
    while True:
        novamente = input("Deseja executar novamente? (s/n): ").lower().strip()
        if novamente in ['s', 'n']:
            break
    
    if novamente == 's':
        main()
    else:
        print("\nObrigado por usar o simulador FIFO!")


if __name__ == "__main__":
    main()
