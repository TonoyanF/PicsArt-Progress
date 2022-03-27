def double(n):
  return n * 2
 
def halve(n):
  if n % 2 == 0:
    return n / 2
   
def fast_mul(m,n):
  if n == 1:
    return m   
  elif halve(n):
    return double(fast_mul(m,halve(n)))  
  return m + double(fast_mul(m,halve(n-1)))
