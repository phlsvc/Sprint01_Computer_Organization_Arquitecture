; --- DEFINIÇÃO DE CONSTANTES ---
LIMIT_TEMP  EQU  60          ; Limite seguro de temperatura (60°C)

AREA |.text|, CODE, READONLY
EXPORT Start

Start
    ; --- PASSO 1: SIMULAÇÃO DA LEITURA DO SENSOR ---
    ; Em um cenário real, leríamos o endereço do ADC. 
    ; Para a simulação, injetamos um valor direto em R1 para testar a lógica.
    MOV  R1, #65             ; Simulando que o sensor detectou 65°C (Anomalia!)

    ; --- PASSO 2: CONTROLE DO PIPELINE (COMPARAÇÃO) ---
    CMP  R1, #LIMIT_TEMP     ; Compara a temperatura atual (R1) com o limite (60)
    
    ; --- PASSO 3: DESVIO CONDICIONAL (BRANCH) ---
    BGE  Corte_Seguranca     ; Se R1 >= 60, desvia o pipeline para o corte de energia

    ; --- PASSO 4: EFICIÊNCIA ENERGÉTICA (SUSTENTABILIDADE) ---
    ; Se a temperatura estiver normal, o processador não precisa gastar energia.
    ; A instrução WFI desliga o clock do núcleo até o próximo ciclo.
    WFI                      ; Wait For Interrupt (Modo Sleep de baixo consumo)
    B    Start               ; Retorna ao início quando acordar

Corte_Seguranca
    ; --- PASSO 5: ATUAÇÃO NO HARDWARE EMBARCADO ---
    MOV  R2, #0              ; R2 vira 0 (Sinal enviado para desligar o relé de carga)
    
Loop_Trava
    B    Loop_Trava          ; Trava o sistema em modo de segurança até o reset manual
