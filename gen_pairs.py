

# python -c 'import random; g = lambda x: random.sample(range(x*10, x*80), 20); print zip(g(4), g(9))'

import random

g = lambda x: random.sample(range(x*10, x*80), 20)

a = g(4)
b = g(9)

for ix in xrange(len(a)):
    print "%d, %d" % (a[ix], b[ix])

# print [ list(c) for c in zip(a, b) ] 


