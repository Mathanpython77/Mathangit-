#Recursion method
def funco(n):
    if (n==1 or n==0):
        return 1
    else:
        return n* funco (n-1)
print(funco(5))

    


        