def pascal(n,m):
    if m == 1 or n == m:
        return 1
    return pascal(n-1,m-1) + pascal(n,m-1)    
