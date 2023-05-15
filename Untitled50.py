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

-----------------------------------------------------

def schet1 ():
    a = int(input("Введите первое число:"))
    a = float(a)
    b = int(input("Введите второе число:"))
    a = float(b)
    c = int(input("Введите третье число:"))
    a = float(c)
    s = int(input("Введите третье число:"))
    s = float(c)
    if a > b < c:
        print (a - b + c - s)
    else:
        print (b + a - c + s)
    return a, b, c, s
a, b, c, s = schet1()
q, w, e, r = schet1()
def schet2 ():
    f = a - q + b - w + c - e + s - r
    g = a + q - b + w - c + e - s + r
    if f == g:
        print(f ** 2)
    else:
        print(a * q - s * r)
    return a, b, c, s
a, b, c, s = schet2()
q, w, e, r = schet2()
