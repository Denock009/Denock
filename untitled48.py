from random import randint
c = 0
a = randint(0, 101)
while True:
    b = int(input())
    c += 1
    if b == a:
        print('Вы угадали')
        print('Количество попыток', c)
        break
    if b > a:
        print('Число больше загаданного')
    else:
        print('Число меньше загаданного')
        
       
---------------------------------------------------------------------

from random import randint
c = 0
a = randint(0, 101)
for _ in range(101):
    b = int(input())
    c += 1
    if b == a:
        print('Вы угадали')
        print('Количество попыток', c)
        break
    if b > a:
        print('Число больше загаданного')
    else:
        print('Число меньше загаданного')

