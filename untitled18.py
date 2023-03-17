a = 10
b = 1
c = 0
while c <= 100:
    c += a
    a = a + a * 0.1
    b +=  1
print(b)
----------------------------------------------------
a = 10
b = 1
c = 0
if c <= 100:
    c += a
    a = a + a * 0.1
    b +=  1
    if c <= 100:
        c += a
        a = a + a * 0.1
        b +=  1
        if c <= 100:
            c += a
            a = a + a * 0.1
            b +=  1
            if c <= 100:
                c += a
                a = a + a * 0.1
                b +=  1
                if c <= 100:
                    c += a
                    a = a + a * 0.1
                    b +=  1
                    if c <= 100:
                        c += a
                        a = a + a * 0.1
                        b +=  1
                        if c <= 100:
                            c += a
                            a = a + a * 0.1
                            b +=  1
                            if c <= 100:
                                c += a
                                a = a + a * 0.1
                                b +=  1
                                if c <= 100:
                                    c += a
                                    a = a + a * 0.1
                                    b +=  1
                                    if c <= 100:
                                        c += a
                                        a = a + a * 0.1
                                        b +=  1
                                        if c <= 100:
                                            c += a
                                            a = a + a * 0.1
                                            b +=  1
                                            if c <= 100:
                                                c += a
                                                a = a + a * 0.1
                                                b +=  1
                                                if c <= 100:
                                                    c += a
                                                    a = a + a * 0.1
                                                    b +=  1
                                                    if c <= 100:
                                                        c += a
                                                        a = a + a * 0.1
                                                        b +=  1
                                                        if c <= 100:
                                                            c += a
                                                            a = a + a * 0.1
                                                            b +=  1
                                                            if c <= 100:
                                                                c += a
                                                                a = a + a * 0.1
                                                                b +=  1
                                                            else:
                                                                print(b)
                                                        else:
                                                            print(b)       
                                                    else:
                                                        print(b)
                                                else:
                                                    print(b)      
                                            else:
                                                print(b)
                                        else:
                                            print(b)       
                                    else:
                                        print(b)
                                else:
                                    print(b)    
                            else:
                                print(b)
                        else:
                            print(b)       
                    else:
                        print(b)
                else:
                    print(b)     
            else:
                print(b)
        else:
            print(b)            
    else:
        print(b)
else:
    print(b)       
