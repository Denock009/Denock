while True:
    x = input('Введите число')
    a = x.isdigit()
    if a == True:
        x = float(x)
        x1 = x * 0.01745329252
        if x > 3.14/4:
            print(1 - x1 ** 3)
        else:
            print(x1 - x1 ** 3 / 6)
        break
    else:
        print('Попробуйте снова')



