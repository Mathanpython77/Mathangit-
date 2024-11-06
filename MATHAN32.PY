#[EXCEPTION HANDLING]
# Except method 17

try:
    a=10
    b=0
    c=a/b
    print(c)
except:
    print("number should not be zero")


#Except method 2
try:
    no1=int(input("enter a no1:"))
    no2=int(input("enter a no2:"))
    c=no1/no2
    print(c)
except ZeroDivisionError:
    print("input should not be erorr")
except ValueError:
    print("check the value")
except:
    print("check the program")

#elsse erorr method 
try:
    no1=int(input("enter a no1:"))
    no2=int(input("enter a no2:"))
    c=no1/no2
    print(c)
except ZeroDivisionError:
    print("input should not be erorr")
except ValueError:
    print("check the value")
except:
    print("check the program")
else:
    print("no error")
finally:
    print("program finisihed")




