# ChargeGrid EcoFirmware: Otimização de Sistemas Embarcados para Eletropostos

> Integrantes
• Felipe alves canazza - RM: 572470
• Eduardo reis - RM: 569727
• Pedro henrique izidoro andreaza - RM: 571107
• Pedro lembruger - RM: 572094
• Gustavo pola - RM: 570114
• caio ceschini - RM: 570798

───

> Problema
Os sistemas de gerenciamento de eletropostos comerciais atuais sofrem com a ineficiência computacional e o desperdício de energia na borda (Edge) . A maioria dessas estações utiliza hardware genérico rodando sistemas operacionais pesados ou interpretadores de alto nível (como Python ou C++ não otimizado) para monitorar os ciclos de carga.

Esse cenário gera dois grandes problemas:
1. Consumo 24/7 Desnecessário: A CPU opera em laços de repetição infinitos (busy-waiting) mantendo o consumo elétrico máximo do chip mesmo quando nenhuma recarga está ativa ou o posto está ocioso.
2. Latência Crítica: A sobrecarga (overhead) de divisão de escopo, gerenciamento de memória e interpretação das linguagens de alto nível atrasa a leitura de sensores em milissegundos preciosos, o que pode retardar o corte de corrente em eventos críticos de superaquecimento de baterias automotivas.

───

> Justificativa
Substituir o processamento genérico de alto nível por rotinas de controle de baixo nível em Assembly resolve diretamente o gargalo energético e de segurança. Ao interagir diretamente com o hardware sem intermediários, reduz-se o número de instruções necessárias para executar uma tarefa, minimiza-se o tráfego no barramento com a memória RAM e ganha-se controle total sobre os estados de suspensão física do chip, alinhando a infraestrutura de mobilidade elétrica às demandas globais de transição energética sustentável.

───

> Proposta de Solução
A solução consiste no desenvolvimento de um firmware de missão crítica dedicado ao loop de proteção térmica e controle de carga dinâmica do eletroposto. Utilizando a linguagem Assembly ARM, a aplicação simula e executa a leitura contínua dos sensores de temperatura dos veículos e atua de forma instantânea na desconexão do relé de energia em caso de anomalias, operando com ultra-baixo consumo e latência em nanossegundos.

───

> Arquitetura Utilizada
• Modelo de Arquitetura:RISC (Reduced Instruction Set Computer).
• Processador Alvo (Simulado): Família ARM Cortex-M (Ex: Cortex-M0+ / M4), padrão da indústria para sistemas embarcados eficientes e controle em tempo real.
• Características Exploradas:
◦ Pipeline Otimizado: Fluxo de instruções desenhado de forma linear para evitar quebras de pipeline (flushing) e erros de previsão de desvios (branch mispredictions).
◦ Registradores Internos: Processamento focado exclusivamente nos registradores internos da CPU (R0, R1, R2), eliminando o uso lento de pilhas de memória RAM.




O motivo de o Python (alto nível) gastar tantos ciclos a mais do que o Assembly
(baixo nível) se resume a três fatores principais de arquitetura de computadores:

1. Camadas de Abstração (Overhead)

Quando você escreve temperatura = 65 em Python, a linguagem não está apenas colocando o número 65 em um pedaço de silício.
Por trás dos panos, o Python precisa:

Criar um objeto do tipo Inteiro na memória RAM.

Alocar memória dinâmica.

Registrar o nome da variável em um dicionário interno da linguagem.

==No Python: Para checar o valor, o processador frequentemente precisa buscar o dado na memória RAM
(ou nos níveis de cache), cruzando o barramento de dados da placa. Isso custa tempo e energia.


==No Assembly: O processador trabalha exclusivamente com os registradores internos (que ficam colados na Unidade Lógica e Aritmética - ULA).
O acesso aos registradores demora menos de 1 ciclo de clock.