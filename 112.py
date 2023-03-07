from math import *
f, l2, l10, s, cos, sin, tan, d, r = factorial, log2, log10, sqrt, cos, sin, tan, degrees, radians
n = ['f', 'l2', 'l10', 's', 'cos', 'sin', 'tan', 'd', 'r']
v = input()
a = v[0]
if n.count(a):
    print(10)
else:
    print(eval(v))

    