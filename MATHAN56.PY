#program to count the number of even and odd numbers from an array of N numbers 
#even_odd_count
a=[]
even_count=0
odd_count=0
n=int(input("enter the total number of elements in the array:"))
for i in range (1,n+1):
    x=int(input("enter the %d element:"%i))
    a.append(x)
for i in range (1,n+1):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("total number of even numbers in the array =",even_count)
print("total number of odd numbers in the array =",odd_count)


