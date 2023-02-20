a=int(input())
b=int(input())
a1=int(input())
b1=int(input())
if (a+b+a1+b1)%2!=0:
    print('NO')
elif a<a1 and b<b1:
    if b%2==0:
        print('YES')
    elif b1==1:
        print('NO')
    else:
        print('YES')
elif a>a1 and b>b1:
    if a%2==0:
        print('YES')
    elif a1==1:
        print('NO')
    else:
        print('YES')
elif a<a1 and b>b1:
    if a+b==a1+b1:
        print('YES')
    else:
        print('NO')
elif a>a1 and b<b1:
    if a+b==a1+b1:
        print('YES')
    else:
        print('NO')

else:
    print('NO')
