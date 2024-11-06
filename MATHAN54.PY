#program to display the first n terms of the fibonacci series 
n=int(input("how many terms?"))
f1=0
f2=1
print("the fibonacci series is")
print(f1)
print(f2)
i=3
while i<=n:
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
    i=i+1

