def schet ():
 a = input("Введите первое число:")
 a = float(a)
 b = input("Введите второе число:")
 b = float(b)
 if a>b:
    print (a-b)
 else:
    print (b-a)
 return a,b
c,d = schet()
e,f = schet()
z,x = schet()

----------------------------------------------------

def schet ():
    a = int(input("Введите первое число:"))
    a = float(a)
    b = int(input("Введите второе число:"))
    a = float(b)
    c = int(input("Введите третье число:"))
    a = float(c)
    if a > b < c:
        print (a - b - c)
    else:
        print (b + a + c)
    return a, b, c
y, u, g = schet()
k, h, p = schet()
t, x, v = schet()
