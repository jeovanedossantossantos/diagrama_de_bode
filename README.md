# diagrama_de_doby

O diagrama de Bode é uma ferramenta gráfica utilizada na engenharia e na teoria de controle para representar a resposta em frequência de sistemas lineares e invariantes no tempo. Ele é composto por dois gráficos separados, ambos plotados em função da frequência:

Diagrama de magnitude: Mostra a magnitude da função de transferência (ou ganho do sistema) em decibéis (dB) versus a frequência em escala logarítmica. A magnitude em decibéis é dada por:

∣H(jω)∣dB=20log10∣H(jω)∣

Diagrama de fase: Exibe a fase da função de transferência em graus versus a frequência em escala logarítmica. A fase é dada por:

∠H(jω)

Os diagramas de Bode são úteis para analisar a estabilidade e o desempenho de sistemas de controle, permitindo a visualização de como o sistema responde a diferentes frequências. Com esses diagramas, é possível identificar facilmente a frequência de corte, o ganho de margem, a margem de fase e outras características importantes do sistema.

Passos para construir um Diagrama de Bode:
Determinação da função de transferência: Obter a função de transferência H(s) do sistema.
Substituição de 𝑠 por jω Onde  s é a variável de Laplace e  ω é a frequência angular em rad/s.
Cálculo da magnitude e fase: Calcular a magnitude ∣H(jω)∣ e a fase ∠H(jω) para uma faixa de frequências.
Plotagem dos gráficos: Plotar a magnitude em dB e a fase em graus em função da frequência em escala logarítmica.
