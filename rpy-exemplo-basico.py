# -*- coding: utf-8 -*-

import rpy2.robjects as robjects

from rpy2.robjects import r

pi = robjects.r['pi']
pi[0]

pi.r_repr()
# pi é o objeto do R
# pi[0] é o valor
# >>> pi
# >>> <FloatVector - Python:0x101ae2710 / R:0x1039724e8>
# >>> [3.141593]

robjects.r.ls(globalenv)
robjects.globalenv["a"] = 123
print(robjects.r.ls(globalenv))
robjects.r.rm("a")
print(robjects.r.ls(globalenv))

from rpy2.robjects import IntVector
from rpy2.robjects import StrVector
from rpy2.robjects import FloatVector

a = IntVector([10])
b = IntVector([15])
print a[0] + b[0]

strings = robjects.StrVector(['abc', 'def'])
integers = robjects.IntVector([1, 2, 3])
floats = robjects.FloatVector([1.1, 2.2, 3.3])


valores = IntVector([6, 7, 4, 3, 2, 0, 0, 6])
valores[4]  # importante notar que python começa de 0
valores[3]  # e o R começa de 1
len(valores)
max(valores)
min(valores)

import ipdb; ipdb.set_trace()

print r.sum(valores)[0]
print r.prod(valores)[0]
print r.sort(valores)
print r.mean(valores)[0]
print r.median(valores)[0]
print r.sd(valores)[0]
print r.var(valores)[0]

valores_python = list(valores)

he = IntVector([10, 2, 23, 11, 14, 35, 46, 32, 13, 51, 27, 49])
ha = he
print r.var(he)[0]
print r.cov(ha, he)[0]
print r.cor(ha, he)[0]

#  funções

sqr = robjects.r('function(x) x^2')
print(sqr)
print(sqr(2))
print(sqr(IntVector([4])))
print(sqr(IntVector([4,4])))

eleva3 = robjects.r('function(a){ return(a*a*a); }')
print(eleva3)
print(eleva3(2))
print(eleva3(IntVector([4])))
print(eleva3(IntVector([4,4])))


# utilitários

r.getwd()
r.setwd("c:/docs/mydir") # lançam exceções de python
r.dir() # Lista arquivos do cwd.

import ipdb; ipdb.set_trace()
