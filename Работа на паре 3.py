a=int(input('Ввудите 3-х значное число:'))
if 99>a or 1000<a:
    print('Ошибка')
    print('Вы пытаетесь ввести не 3-х значное число')
else:
    b=a//100
    c=a%100//10
    v=a%10
    g=v*100+c*10+b
    print('Разность между вашим 3-х значным числом и числом, составленным из тех же цифр, но взятых в обратном порядке:', a-g)