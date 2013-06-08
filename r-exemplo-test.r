import rpy2.robjects as R
from rpy2.robjects import IntVector


# Dez cobaias foram submetidas ao tratamento de engorda com certa ração.
# Os pesos em gramas, antes e após o teste são dados a seguir
# (supõe-se que provenham de distribuições normais).
# A 1% de significância, podemos concluir que o uso da ração contribuiu para o aumento do peso médio dos animais?

# Antes
# 635, 704, 662, 560, 603, 745, 698, 575, 633, 669
# Depois
# 640, 712, 681, 558, 610, 740, 707, 585, 635, 682

# media = antes - depois
# H0: media = 0
# H1: media < 0

# t test
antes <- c(635, 704, 662, 560, 603, 745, 698, 575, 633, 669)
depois <- c(640, 712, 681, 558, 610, 740, 707, 585, 635, 682)
result <- t.test(antes, depois, alternative='less', conf.level = 0.99, paired=TRUE)

result

if (result[["p.value"]] < 0.01) {
    final_result = 1;
}else{
    final_result = 0;
}

if (final_result==1) {
    print('Rejeitamos a Hipotese Nula');
}else{
    print('Existem evidências para não rejeitarmos a hipótese nula.');
}

# Assim, REJEITAMOS H0 a 1% de significância.
# Assim, concluímos com 99% de confiança (ou uma chance de erro de 1%) que a dieta contribuiu para o aumento do peso médio dos animais.
