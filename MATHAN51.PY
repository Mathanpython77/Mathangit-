#temp -conversion
print("1.frahrenheit to celsius coversion")
print("2.celsius to frahrenheit conversion")
ch=int(input("enter your choice:"))
if ch ==1:
    f=int(input("enter thye temperature in fahrenheit:"))
    c=(5/9)*(f-32)
    print(f,"degree fahrenheit is equal to %.2f"%c,"degree celsius")
elif ch ==2:
    c=int(input("enter the temperature in celsius:"))
    f=(9/5)*c+32
    print(c,"dgree celswius is equal to %.2f"%f,"degree fahrenheit")

else:
    print("wrong choice")

