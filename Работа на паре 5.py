a=int(input('Ввудите 6-х значное число:'))
if a>99999 and a<1000000:
    a1=a//100000
    a2=a//10000%10
    a3=a//1000%10
    a4=a//100%10
    a5=a//10%10
    a6=a%10
    if a1==2 or a2==2 or a3==2 or a4==2 or a5==2 or a6==2:
        print('В данном числе имеется цифра 2')
    else:
        print('В данном числе нет цифры 2')
else:
    print('Ошибка')
    print('Вы пытаетесь ввести не 6-х значное число')




