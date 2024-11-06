#program to find the factorial of a number using recursion
def fact(m):
    if m<=1:
        return 1
    else:
        return m*fact(m-1)
    
#main program

n=int(input("enter the valve of n:"))
f=fact(n)
print("the factorial of",n,"is",f)