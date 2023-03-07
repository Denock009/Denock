from math import *
f, l2, l10, s, cos, sin, tan, d, r = factorial, log2, log10, sqrt, cos, sin, tan, degrees, radians
n = list('f, l2, l10, s, cos, sin, tan, d, r')
v = input()
if len(v) > 2 and (v.find(n)) != 1:
    print(eval(v))
else:
    print('f = factorial (нахождение факториала)', 'l2 = log2 (нахождение лагорифна по основанию 2)', 'l10 = log10 (нахождение лагорифна по основанию 10)', 's = sqrt (нахождение квадратного корня)', 'cos = cos (нахождение косинуса)', 'sin = sin (нахождение синуса)', 'tan = tan (нахождение тангенса)', 'd = degrees (конвертация радианы в градусы)', 'r = radians (конвертация градусы в радианы)', sep='\n')
    print(10)
    
