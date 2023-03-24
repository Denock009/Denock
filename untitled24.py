a = int(input())
if a % 4 == 0:
    if a % 100 != 0:
        print('Год высокосный')
    elif a % 400 == 0:
        print('Год высокосный')
    else:    
        print('Год обычный')
    
else: 
    print('Год обычный')