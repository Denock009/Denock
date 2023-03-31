a, b = int(input()), int(input())
if 99<a<1000:
    a = str(a)
    a1, a2, a3 = a[0], a[1], a[2]
    c = int(a1 + a2 + a3)
    if c > b:
        print('Cброс')
        a = 0
    else:
        print('Сегодня не сломался -', b)