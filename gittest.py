n = 20

for i in range(n):
    if  n/2 >= i+1:
     print(' '*(n-i)+'*'*(2*i-1))

    elif n/2 < i+1:
        print(' '*i+'*'*(2*(n-i)-1))