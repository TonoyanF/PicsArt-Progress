def f_rec(n):
  if n < 3 and n >= 0:
    return n
  else:
    return  f_rec(n-1) + f_rec(n-2) + f_rec(n-3)
f_rec(10) 

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
 

def f_3(n,a,b,c):
    if n == 0:
        return a
    else:
        return f_3(n-1 , b , c , a + b + c)    
