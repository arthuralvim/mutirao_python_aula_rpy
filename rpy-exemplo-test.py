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


# t test
antes = IntVector([635, 704, 662, 560, 603, 745, 698, 575, 633, 669])
depois = IntVector([640, 712, 681, 558, 610, 740, 707, 585, 635, 682])
result = R.r['t.test'](antes, depois, alternative='two.sided', alpha=0.01, paired=True)
import ipdb; ipdb.set_trace()
print result.rx('p.value')[0][0]
print result.rx('statistic')[0][0]
print result.rx('parameter')[0][0]
print result.rx('estimate')[0][0]

final_result = 1 if result.rx('p.value')[0][0] < 0.01 else 0

if final_result==1:
    print 'Rejeitamos a Hipotese Nula'
else:
    print 'Existem evidências para não rejeitarmos a hipótese nula.'

# Assim, REJEITAMOS H0 a 1% de significância.
# Assim, concluímos com 99% de confiança (ou uma chance de erro de 1%) que a dieta contribuiu para o aumento do peso médio dos animais.

import ipdb; ipdb.set_trace()
