#funtion to calculate the area of a rectangle
def rectangle():
    i=float(input("enter the length of a rectangle:"))
    b=float(input("enter the breadth of a rectangle:"))
    r_area=i*b
    print("\nthe area of a rectangle is :%0.2f"%r_area)
    return

#function to calculate the area of a square
def square():
    s=int(input("enter the side length of a square:"))
    s_area=s*s
    print("\nthe area of a square is :",s_area)
    return

#funtion to calculate the area of a circel

def circle():
    pi=3.14
    r=float(input("enter the radius of a circle:"))
    c_area=pi*r*r
    print("\nthe area of a cicle is :%0.f"%c_area)
    return

#funtion to calculate the area of a triangle
def triangle():
    a=int(input("enter the first side of a triangle :"))
    b=int(input("enter a second side of a triangle :"))
    c=int(input("enter the third side of a triangle :"))
    s=(a+b+c)/2
    t_area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("the area of a triangle is :%0.2f%t_area")
    return
#main program
print("1.rectangle")
print("2.square")
print("3.circle") 
print("4.triangle")
shape =input("enter the shape you want to calculate the area:")
if shape=="rectangle":
    rectangle()
elif shape =="square":
    square()
elif shape=="circle":
    circle()
elif shape =="triangle":
    triangle()
else:
    print("select a valid shape")
 