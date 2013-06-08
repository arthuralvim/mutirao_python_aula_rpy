# -*- coding: utf-8 -*-


from rpy2.robjects import r
from rpy2.robjects import IntVector

x = IntVector(range(9))
y = IntVector(range(9))

import ipdb; ipdb.set_trace()

r.png('figura1.png')
r.plot(x, y)
r['dev.off']()

r.png('figura2.jpeg')
r.plot(x, y, xlab='x', ylab='y', main='Minha plotagem', type='l')
r['dev.off']()

r.png('figura3.pdf')
normal = r.rnorm(500, 0, 1)
r.hist(normal)
r['dev.off']()
