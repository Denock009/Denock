from math import *
k = input('Если вы хотите производить операции с двумя числами введите 2, а если с одним числом то введите 1')
if k == 2:
    a, b, c = input('Введите первое число'), input('Введите оператор'), input('Введите второе число')
    if b == '**':
        print(a ** c )
    elif b == '//':
        print(a // c)
    elif b == '/':
        print(a / c)
    elif b == '%':
        print(a % c)
    elif b == '*':
        print(a * c)
    elif b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
else:
    a, b = int(input()), input()
    if '!' in b:
        print(factorial(a))
    