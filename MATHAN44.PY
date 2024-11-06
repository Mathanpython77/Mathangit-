#
def celsius_to_fahrenheit(celsius):
    fahrenheit =(celsius * 9/5)+32
    return fahrenheit

celsius = float(input("enter temperature in celsius"))

fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}deg C is equal to {fahrenheit}deg f")

#
def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

fahrenheit = float(input("enter temperature in celsius"))

celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}deg  is equal to {celsius}deg C")

