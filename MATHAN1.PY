#prime or composite
prime = True
num=int(input("enter a number "))
print(num)
for i in range(2,num):
    if(num%2==0):
        prime=False
        break

if(prime):
    print(F"{num} is prime number")
else:
    print(F"{num} is composite number")
























    


