P = int(input())
a = 2
b = P ** 2
for i in range(b):
    if a ** 0.5 >= P:
        break
    print(a ** 0.5)
    a += 1

---------------------------------------------------

a = int(input())
b = int(input())
for i in range(a+1, b):
    print(i)
    
---------------------------------------------------

a = int(input())
b = int(input())
for i in range(a+1, b)[::-1]:
    print(i)
    
---------------------------------------------------

from math import ceil
n = int(input())
k = n / 2.9
print(ceil(k))U
    
    
