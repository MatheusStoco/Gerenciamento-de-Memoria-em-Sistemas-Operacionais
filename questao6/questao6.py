# Questão 3 - Simulação dos Algoritmos FIFO e LRU de Substituição de Página
# Autor: Lucas Vaz (adaptado)

# ========================================================================
# BLOCO 1: IMPLEMENTAÇÃO DO ALGORITMO FIFO
# ========================================================================
class FIFOPageReplacement:
    """
    Implementa o algoritmo FIFO (First In First Out) para substituição de páginas.
    A página mais antiga na memória é sempre a primeira a ser removida.
    """
    
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0
        self.page_hits = 0
        self.historico = []
    
    def processar_referencia(self, pagina, timestamp):
        """Processa uma referência de página usando FIFO"""
        if pagina in self.frames:
            self.page_hits += 1
            self.historico.append({
                'pagina': pagina,
                'frames': self.frames.copy(),
                'tipo': 'Hit',
                'substituida': None
            })
            return False, None
        
        self.page_faults += 1
        pagina_substituida = None
        
        if len(self.frames) < self.num_frames:
            self.frames.append(pagina)
        else:
            pagina_substituida = self.frames.pop(0)
            self.frames.append(pagina)
        
        self.historico.append({
            'pagina': pagina,
            'frames': self.frames.copy(),
            'tipo': 'Fault',
            'substituida': pagina_substituida
        })
        
        return True, pagina_substituida
    
    def simular(self, sequencia_paginas):
        """Executa a simulação completa"""
        self.page_faults = 0
        self.page_hits = 0
        self.frames = []
        self.historico = []
        
        for i, pagina in enumerate(sequencia_paginas):
            self.processar_referencia(pagina, i)
        
        return self.get_estatisticas()
    
    def get_estatisticas(self):
        """Retorna estatísticas da simulação"""
        total = self.page_faults + self.page_hits
        return {
            'algoritmo': 'FIFO',
            'page_faults': self.page_faults,
            'page_hits': self.page_hits,
            'total_referencias': total,
            'taxa_falta': (self.page_faults / total * 100) if total > 0 else 0,
            'taxa_acerto': (self.page_hits / total * 100) if total > 0 else 0,
            'historico': self.historico
        }


# ========================================================================
# BLOCO 2: IMPLEMENTAÇÃO DO ALGORITMO LRU
# ========================================================================
class LRUPageReplacement:
    """
    Implementa o algoritmo LRU (Least Recently Used) para substituição de páginas.
    
    Estratégia: Mantém um dicionário com timestamps de último uso de cada página.
    Quando necessário substituir, remove a página com menor timestamp (menos usada).
    
    Estrutura de dados:
    - frames: lista das páginas na memória
    - uso_timestamps: dicionário {pagina: timestamp_ultimo_uso}
    """
    
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.uso_timestamps = {}  # Mapeia página -> timestamp do último uso
        self.page_faults = 0
        self.page_hits = 0
        self.historico = []
    
    def processar_referencia(self, pagina, timestamp):
        """
        Processa uma referência de página usando LRU.
        
        Args:
            pagina: número da página referenciada
            timestamp: momento da referência (usado para determinar recência)
        """
        # Atualiza timestamp sempre que a página é referenciada
        self.uso_timestamps[pagina] = timestamp
        
        # Verifica se é Page Hit
        if pagina in self.frames:
            self.page_hits += 1
            self.historico.append({
                'pagina': pagina,
                'frames': self.frames.copy(),
                'tipo': 'Hit',
                'substituida': None,
                'timestamps': self.uso_timestamps.copy()
            })
            return False, None
        
        # Page Fault
        self.page_faults += 1
        pagina_substituida = None
        
        if len(self.frames) < self.num_frames:
            # Há espaço disponível, apenas adiciona
            self.frames.append(pagina)
        else:
            # Frames cheios: encontra a página menos recentemente usada
            pagina_lru = self._encontrar_lru()
            pagina_substituida = pagina_lru
            
            # Remove a página LRU dos frames e do registro de timestamps
            self.frames.remove(pagina_lru)
            del self.uso_timestamps[pagina_lru]
            
            # Adiciona a nova página
            self.frames.append(pagina)
        
        self.historico.append({
            'pagina': pagina,
            'frames': self.frames.copy(),
            'tipo': 'Fault',
            'substituida': pagina_substituida,
            'timestamps': self.uso_timestamps.copy()
        })
        
        return True, pagina_substituida
    
    def _encontrar_lru(self):
        """
        Encontra a página menos recentemente usada entre as páginas nos frames.
        
        Returns:
            Número da página com menor timestamp (LRU)
        """
        # Filtra apenas páginas que estão nos frames
        timestamps_frames = {p: self.uso_timestamps[p] for p in self.frames}
        
        # Retorna a página com menor timestamp
        return min(timestamps_frames, key=timestamps_frames.get)
    
    def simular(self, sequencia_paginas):
        """Executa a simulação completa"""
        self.page_faults = 0
        self.page_hits = 0
        self.frames = []
        self.uso_timestamps = {}
        self.historico = []
        
        for i, pagina in enumerate(sequencia_paginas):
            self.processar_referencia(pagina, i)
        
        return self.get_estatisticas()
    
    def get_estatisticas(self):
        """Retorna estatísticas da simulação"""
        total = self.page_faults + self.page_hits
        return {
            'algoritmo': 'LRU',
            'page_faults': self.page_faults,
            'page_hits': self.page_hits,
            'total_referencias': total,
            'taxa_falta': (self.page_faults / total * 100) if total > 0 else 0,
            'taxa_acerto': (self.page_hits / total * 100) if total > 0 else 0,
            'historico': self.historico
        }


# ========================================================================
# BLOCO 3: FUNÇÕES DE VISUALIZAÇÃO E ANÁLISE
# ========================================================================
def exibir_estatisticas(stats):
    """Exibe estatísticas de uma simulação"""
    print(f"\n{'=' * 70}")
    print(f"ESTATÍSTICAS - {stats['algoritmo']}")
    print(f"{'=' * 70}")
    print(f"Total de referências:        {stats['total_referencias']}")
    print(f"Page Faults (faltas):        {stats['page_faults']}")
    print(f"Page Hits (acertos):         {stats['page_hits']}")
    print(f"Taxa de falta:               {stats['taxa_falta']:.2f}%")
    print(f"Taxa de acerto:              {stats['taxa_acerto']:.2f}%")
    print(f"{'=' * 70}")


def analise_comparativa(stats_fifo, stats_lru):
    """
    Realiza análise comparativa crítica entre FIFO e LRU.
    """
    print("\n" + "=" * 90)
    print("ANÁLISE COMPARATIVA: FIFO vs LRU")
    print("=" * 90)
    
    # Tabela comparativa
    print(f"\n{'Métrica':<30} | {'FIFO':>15} | {'LRU':>15} | {'Diferença':>15}")
    print("-" * 90)
    
    metricas = [
        ('Total de Referências', 'total_referencias', ''),
        ('Page Faults', 'page_faults', ''),
        ('Page Hits', 'page_hits', ''),
        ('Taxa de Falta (%)', 'taxa_falta', '.2f'),
        ('Taxa de Acerto (%)', 'taxa_acerto', '.2f')
    ]
    
    for nome, chave, fmt in metricas:
        val_fifo = stats_fifo[chave]
        val_lru = stats_lru[chave]
        diff = val_lru - val_fifo
        
        if fmt:
            fifo_str = f"{val_fifo:{fmt}}"
            lru_str = f"{val_lru:{fmt}}"
            diff_str = f"{diff:+{fmt}}"
        else:
            fifo_str = f"{val_fifo}"
            lru_str = f"{val_lru}"
            diff_str = f"{diff:+d}"
        
        print(f"{nome:<30} | {fifo_str:>15} | {lru_str:>15} | {diff_str:>15}")
    
    # Análise crítica
    print("\n" + "=" * 90)
    print("ANÁLISE CRÍTICA")
    print("=" * 90)
    
    diff_faults = stats_lru['page_faults'] - stats_fifo['page_faults']
    melhoria_percentual = (diff_faults / stats_fifo['page_faults'] * 100) if stats_fifo['page_faults'] > 0 else 0
    
    if diff_faults < 0:
        print(f"✓ LRU TEVE MELHOR DESEMPENHO:")
        print(f"  - {abs(diff_faults)} faltas de página a menos que FIFO")
        print(f"  - Redução de {abs(melhoria_percentual):.2f}% nas faltas")
    elif diff_faults > 0:
        print(f"✗ FIFO TEVE MELHOR DESEMPENHO:")
        print(f"  - LRU teve {diff_faults} faltas a mais")
        print(f"  - Aumento de {melhoria_percentual:.2f}% nas faltas")
    else:
        print("⚬ EMPATE: Ambos algoritmos tiveram o mesmo número de faltas")
    
    print("\nCONSIDERAÇÕES TEÓRICAS:")
    print("-" * 90)
    print("• LRU (Least Recently Used):")
    print("  + Explora localidade temporal: mantém páginas usadas recentemente")
    print("  + Geralmente mais eficiente para workloads com padrões de acesso")
    print("  + Adapta-se melhor a mudanças no padrão de referências")
    print("  - Overhead computacional: precisa rastrear tempo de uso")
    print("  - Mais complexo de implementar em hardware real")
    
    print("\n• FIFO (First In First Out):")
    print("  + Simples de implementar: apenas uma fila")
    print("  + Baixo overhead: não precisa rastrear histórico de uso")
    print("  + Previsível e determinístico")
    print("  - Pode remover páginas frequentemente usadas")
    print("  - Sofre da 'Anomalia de Belady': mais frames pode = mais faltas")
    
    print("\nRESULTADOS NESTA SIMULAÇÃO:")
    print("-" * 90)
    
    if diff_faults < 0:
        print("• LRU demonstrou superioridade ao explorar a localidade temporal")
        print("• A sequência apresentou padrões de reuso que beneficiaram o LRU")
    elif diff_faults > 0:
        print("• Caso incomum: FIFO superou LRU nesta sequência específica")
        print("• Pode indicar padrão de acesso sequencial sem reuso significativo")
    else:
        print("• Para esta sequência, ambos algoritmos foram equivalentes")
        print("• Pode indicar que não houve oportunidade de explorar localidade temporal")
    
    print("=" * 90)


# ========================================================================
# BLOCO 4: FUNÇÃO PRINCIPAL E INTERFACE DO USUÁRIO
# ========================================================================
def main():
    print("\n" + "=" * 90)
    print("SIMULADOR DE SUBSTITUIÇÃO DE PÁGINAS: FIFO vs LRU")
    print("=" * 90)
    
    # Entrada: número de frames
    while True:
        try:
            num_frames = int(input("\nDigite o número de frames disponíveis: "))
            if num_frames <= 0:
                print("O número de frames deve ser maior que 0. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    
    # Entrada: sequência de referências
    print("\nDigite a sequência de referências a páginas.")
    print("Separe os números por vírgula ou espaço.")
    print("Exemplo: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2")
    
    while True:
        try:
            entrada = input("Sequência: ")
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
    
    # Executa ambas as simulações
    print(f"\nExecutando simulações com {num_frames} frames...")
    print(f"Sequência: {sequencia}")
    
    fifo = FIFOPageReplacement(num_frames)
    lru = LRUPageReplacement(num_frames)
    
    stats_fifo = fifo.simular(sequencia)
    stats_lru = lru.simular(sequencia)
    
    # Opção de visualização detalhada
    print("\nDeseja visualizar o passo a passo das simulações?")
    mostrar_detalhes = input("(s/n): ").lower().strip() == 's'
    
    if mostrar_detalhes:
        exibir_simulacao_detalhada(stats_fifo)
        exibir_simulacao_detalhada(stats_lru, mostrar_timestamps=True)
    
    # Exibe estatísticas
    exibir_estatisticas(stats_fifo)
    exibir_estatisticas(stats_lru)
    
    # Análise comparativa
    analise_comparativa(stats_fifo, stats_lru)
    
    # Repetir simulação
    print()
    novamente = input("Deseja executar nova simulação? (s/n): ").lower().strip()
    if novamente == 's':
        main()
    else:
        print("\nObrigado por usar o simulador!")


if __name__ == "__main__":
    main()