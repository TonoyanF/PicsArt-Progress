def f_iter(n):
    a = 0
    b = 1
    c = 2
    while n > 0:
        temp = a + b + c
        a = b
        b = c
        c = temp
        n -= 1   
    return a  
f_iter(5)