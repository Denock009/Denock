a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
if b1==a2:
    print(b1)
elif b1<a2:
    print('пустое множество')
elif a1>=a2:
    if b1<=b2:
        print(a1, b1)
    else:
        if a1==b2:
            print(a1)
        else:
            if b1>a2 and a1>b2:
                print('пустое множество')
            else:
                print(a1, b2)
        
elif b1>=b2:
    if b1>a2:
        print(a2, b2)
    else:
        print(b1, a2)
else:
    print(a2, b1)