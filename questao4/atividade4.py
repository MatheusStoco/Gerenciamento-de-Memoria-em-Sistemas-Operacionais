import gc  # Importa o módulo do Garbage Collector (Coletor de Lixo)
import sys  # Importa o módulo 'sys' para usar o 'getrefcount'
import time # Importa o módulo 'time' apenas para a pausa dramática no cenário 2


#----------------------------------------------------------------------
# 1. DEFINIÇÃO DA CLASSE DE DEMONSTRAÇÃO
#----------------------------------------------------------------------


class DemoObjeto:
    """
    Uma classe de demonstração.
    O único propósito desta classe é nos avisar (imprimindo no console)
    exatamente quando ela é criada (__init__) e quando ela é destruída (__del__).
    """
   
    def __init__(self, nome):
        """
        Este é o "construtor". É chamado assim que o objeto é criado na memória.
        ex: obj = DemoObjeto('MeuObj')
        """
        self.nome = nome
        # Alocamos uma grande quantidade de dados (10 milhões de bytes)
        # para simular um objeto que ocupa uma memória significativa.
        self.dados = bytearray(10_000_000)
       
        # Imprime uma mensagem clara indicando que o objeto nasceu.
        print(f"Objeto '{self.nome}' CRIADO. (id: {id(self)})")


    def __del__(self):
        """
        Este é o "destrutor". É chamado pelo Python automaticamente
        logo ANTES do objeto ser permanentemente apagado da memória.
       
        No Cenário 1, ele será chamado imediatamente.
        Nos Cenários 2/3, ele só será chamado pelo Garbage Collector (gc).
        """
        # Imprime uma mensagem clara indicando que o objeto morreu.
        print(f"Objeto '{self.nome}' DESTRUÍDO. (id: {id(self)}) ---")


# --- FIM DA CLASSE ---




#----------------------------------------------------------------------
# CENÁRIO 1: O Mecanismo Padrão (Contagem de Referências)
#----------------------------------------------------------------------


def cenario_1_contagem_referencias():
    """
    Demonstra a Contagem de Referências.
    Objetos são destruídos IMEDIATAMENTE quando sua contagem de referências chega a 0.
    """
    print("\n" + "="*60)
    print("=== CENÁRIO 1: Contagem de Referências (Destruição Automática) ===")
    print("="*60)
   
    print("1. Criando 'obj_cenario_1'...")
    # Um objeto é criado. Sua contagem de referências é 1 (a variável 'obj_cenario_1')
    obj_cenario_1 = DemoObjeto("A (Cenário 1)")
   
    # sys.getrefcount() nos mostra a contagem de referências.
    # NOTA: O valor é sempre +1 do que esperamos, pois a própria função
    # 'getrefcount()' precisa criar uma referência temporária para "olhar" o objeto.
    print(f"   Refs de 'A': {sys.getrefcount(obj_cenario_1)} (Esperado: 1 + 1 da função = 2)")
   
    print("\n2. Criando 'ref_extra' para o mesmo objeto...")
    # Criamos uma segunda variável apontando para o MESMO objeto.
    # A contagem de referências do objeto agora é 2.
    ref_extra = obj_cenario_1
    print(f"   Refs de 'A': {sys.getrefcount(obj_cenario_1)} (Esperado: 2 + 1 da função = 3)")


    print("\n3. Removendo a 'ref_extra' (atribuindo None)...")
    # Remover uma referência (seja com 'del' ou atribuindo None)
    # decrementa (subtrai 1) da contagem de referências.
    # A contagem agora volta a ser 1.
    ref_extra = None
    print(f"   Refs de 'A': {sys.getrefcount(obj_cenario_1)} (Esperado: 1 + 1 da função = 2)")


    print("\n4. Removendo a referência final 'obj_cenario_1'...")
    # Removemos a última referência que apontava para o objeto.
    # A contagem de referências do objeto chega a 0.
    obj_cenario_1 = None
   
    # No exato momento em que a contagem chega a 0, o Python
    # chama o __del__ e libera a memória.
    # A mensagem "DESTRUÍDO" deve aparecer IMEDIATAMENTE acima desta linha.
    print("\nFinal do Cenário 1. O Objeto 'A' já deve ter sido destruído.")




#----------------------------------------------------------------------
# CENÁRIOS 2 e 3: O Problema (Ciclos) e a Solução (Garbage Collector)
#----------------------------------------------------------------------


def cenario_2_e_3_ciclos_e_gc():
    """
    Demonstra a FALHA da Contagem de Referências (Cenário 2) e
    a SOLUÇÃO do Coletor Geracional (Cenário 3).
    """
    print("\n" + "="*60)
    print("=== CENÁRIO 2: Referências Circulares (Falha da Contagem) ===")
    print("="*60)
   
    # --- Parte 2a: Ciclo entre dois objetos (B <-> C) ---
    print("1. Criando 'obj_B' e 'obj_C'...")
    obj_B = DemoObjeto("B (Ciclo)")
    obj_C = DemoObjeto("C (Ciclo)")


    print("\n2. Criando o ciclo: B aponta para C, C aponta para B")
    # Usamos atribuição direta. Não precisamos de métodos na classe para isso.
    obj_B.ponteiro_para_outro = obj_C
    obj_C.ponteiro_para_outro = obj_B
    # Contagens atuais:
    # Objeto B: Ref de 'obj_B' + Ref de 'obj_C.ponteiro_para_outro' = 2
    # Objeto C: Ref de 'obj_C' + Ref de 'obj_B.ponteiro_para_outro' = 2
   
    # --- Parte 2b: Ciclo de auto-referência (D -> D) ---
    print("\n3. Criando 'obj_D' com auto-referência...")
    obj_D = DemoObjeto("D (Auto-Ciclo)")
   
    print("4. Criando o ciclo: D aponta para si mesmo")
    obj_D.ponteiro_para_si_mesmo = obj_D
    # Contagem atual:
    # Objeto D: Ref de 'obj_D' + Ref de 'obj_D.ponteiro_para_si_mesmo' = 2
   
    print(f"\nRefs de 'B' (antes de deletar): {sys.getrefcount(obj_B) - 1}") # Subtrai 1 da func
    print(f"Refs de 'C' (antes de deletar): {sys.getrefcount(obj_C) - 1}")
    print(f"Refs de 'D' (antes de deletar): {sys.getrefcount(obj_D) - 1}")


    print("\n5. Removendo TODAS as referências externas (variáveis)...")
    # Vamos remover as variáveis 'obj_B', 'obj_C' e 'obj_D'.
    obj_B = None
    obj_C = None
    obj_D = None


    # O que acontece com as contagens?
    # Objeto B: A ref 'obj_B' some. Contagem cai de 2 para 1. (Ainda é > 0)
    # Objeto C: A ref 'obj_C' some. Contagem cai de 2 para 1. (Ainda é > 0)
    # Objeto D: A ref 'obj_D' some. Contagem cai de 2 para 1. (Ainda é > 0)
   
    print("\n!!! ATENÇÃO: NENHUMA MENSAGEM DE 'DESTRUÍDO' APARECEU !!!")
    print("   Os objetos B, C e D ainda estão na memória.")
    print("   Eles estão inacessíveis (nenhuma variável externa os alcança).")
    print("   Mas suas contagens de referência são 1, então o mecanismo padrão FALHOU.")
    print("   Isso é um 'vazamento de memória' (memory leak) temporário.")
   
    time.sleep(1) # Pausa para clareza


    # --- CENÁRIO 3: A SOLUÇÃO ---
    print("\n" + "="*60)
    print("=== CENÁRIO 3: Coletor Geracional (A Solução) ===")
    print("="*60)
    print("O Coletor Geracional (gc) é o 'detetive' do Python.")
    print("Seu trabalho é rodar periodicamente para encontrar essas 'ilhas' de")
    print("objetos inacessíveis (ciclos) e limpá-los.")
   
    print("\nForçando o 'detetive' a rodar agora com gc.collect()...")
   
    # gc.collect() força uma execução de todos os níveis do coletor geracional.
    # Ele retorna o número de objetos que encontrou e conseguiu limpar.
    objetos_coletados = gc.collect()
   
    # As mensagens "DESTRUÍDO" para B, C e D devem aparecer IMEDIATAMENTE
    # acima desta linha, pois o gc quebrou os ciclos e os limpou.
   
    print(f"\nColeta concluída. Total de objetos inalcançáveis coletados: {objetos_coletados}")
    print("Final do Cenário 3.")




#----------------------------------------------------------------------
# 4. MOSTRAR ESTATÍSTICAS FINAIS DO GC
#----------------------------------------------------------------------


def mostrar_estatisticas_finais():
    """
    Exibe as estatísticas acumuladas pelo módulo 'gc'.
    """
    print("\n" + "="*60)
    print("=== ESTATÍSTICAS FINAIS DO GARBAGE COLLECTOR (gc.get_stats()) ===")
    print("="*60)
    print("O GC mantém estatísticas sobre suas execuções.")
   
    # gc.get_stats() retorna uma lista de 3 dicionários, um para cada "geração".
    # Geração 0: Objetos novos (coletada mais frequentemente).
    # Geração 1: Objetos que sobreviveram à Geração 0.
    # Geração 2: Objetos que sobreviveram à Geração 1 (coletada com menos frequência).
   
    stats = gc.get_stats()
   
    print(f"\nGer. 0 (Jovem): {stats[0]}")
    print(f"Ger. 1 (Média): {stats[1]}")
    print(f"Ger. 2 (Velha): {stats[2]}")
   
    # 'collections': Quantas vezes essa geração foi verificada.
    # 'collected': Quantos objetos foram limpos dessa geração.
    # 'uncollectable': Objetos que o GC encontrou mas não pôde limpar (raro).




#----------------------------------------------------------------------
# PONTO DE ENTRADA PRINCIPAL DO SCRIPT
#----------------------------------------------------------------------


def executar_demonstracao_completa():
    """
    Função principal que organiza a execução de todos os cenários.
    """
   
    # É uma boa prática desativar o GC automático ANTES de
    # iniciar uma demonstração, para que ele não rode no meio
    # do nosso Cenário 2 e "estrague" a demonstração da falha.
    if gc.isenabled():
        print("Desativando o GC automático para a demonstração...")
        gc.disable()
       
    # Executa o Cenário 1
    cenario_1_contagem_referencias()
   
    # Executa os Cenários 2 e 3
    cenario_2_e_3_ciclos_e_gc()
   
    # Mostra as estatísticas
    mostrar_estatisticas_finais()


    # Reativa o GC automático no final
    if not gc.isenabled():
        print("\nReativando o GC automático.")
        gc.enable()




# Este é o padrão do Python. O código só roda se este
# arquivo for executado diretamente (e não importado por outro).
if __name__ == "__main__":
    executar_demonstracao_completa()