def pascal(n,m):
    if 1 in (n,m) or n == m:
        return 1
    else:
        return pascal(n-1,m-1) + pascal(n,m-1)    
