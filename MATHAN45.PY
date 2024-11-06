#Calculate the area of triangle

a=float(input("enter length of 1st side:"))
b=float(input("enter length of 2nd side:"))
c=float(input("enter length of 3rd side:"))
 
#calculate semi-perimeter
s=(a+b+c)/2

#calculate area
area =(s*(s-a)*(s-b)*(s-c))** 0.5
print("\narea of the triangle is ",area)