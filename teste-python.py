import time

def simulacao_alto_nivel():
    print("--- CENÁRIO A: ALTO NÍVEL (PYTHON/C++) ---")
    # Em alto nível, criar variáveis aloca espaço na memória e gera overhead
    temperatura_sensor = 65  
    limite_seguro = 60
    status_carregador = 1
    
    # Simulação de ciclos de clock estimados que o interpretador/compilador gasta
    # Para gerenciar escopo, buscar na memória e executar expressões
    instrucoes_geradas = 120  # Alto nível gera muitas instruções de máquina secundárias
    ciclos_por_instrucao = 4   # Média de ciclos por instrução complexa em CISC/Alto nível
    total_ciclos_alto_nivel = instrucoes_geradas * ciclos_por_instrucao
    
    print(f"[Loop Ativo] Verificando temperatura: {temperatura_sensor}°C")
    if temperatura_sensor >= limite_seguro:
        status_carregador = 0
        print(f"[ALERTA] Cortando energia! Status do Relé: {status_carregador}")
    
    print(f"-> Total estimado de ciclos de CPU gastos: {total_ciclos_alto_nivel} ciclos.")
    print("-> Comportamento em espera: Loop infinito rodando a 100% da CPU.\n")
    return total_ciclos_alto_nivel


def simulacao_baixo_nivel_assembly():
    print("--- CENÁRIO B: BAIXO NÍVEL (NOSSO ASSEMBLY) ---")
    # No Assembly que criamos, usamos direto os registradores internos (R1 e R2)
    # Cada instrução RISC é simples e consome pouquíssimos ciclos
    
    # MOV R1, #65       -> 1 ciclo
    # CMP R1, #60       -> 1 ciclo
    # BGE Corte         -> 2 ciclos (quando há o desvio)
    # MOV R2, #0        -> 1 ciclo
    total_ciclos_assembly = 1 + 1 + 2 + 1
    
    print("[Registrador R1] Armazenou 65°C instantaneamente.")
    print("[Comparação Física] R1 >= 60 detectado direto no hardware.")
    print("[Registrador R2] Alterado para 0 (Corte em nanossegundos).")
    
    print(f"-> Total real de ciclos de CPU gastos: {total_ciclos_assembly} ciclos.")
    print("-> Comportamento em espera: Instrução 'WFI' desliga o clock (0 ciclos / Sleep).\n")
    return total_ciclos_assembly


# Executando o comparador
ciclos_alto = simulacao_alto_nivel()
ciclos_baixo = simulacao_baixo_nivel_assembly()

ganho_eficiencia = (ciclos_alto / ciclos_baixo)
print("=== RESULTADO DA COMPARAÇÃO ===")
print(f"A solução em Assembly é aproximadamente {ganho_eficiencia:.1f} vezes mais rápida em ciclos de CPU para o corte de segurança.")
