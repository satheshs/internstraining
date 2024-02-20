def c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("What do you wants to convert?")
print("1.Celsius to Fahrenheit")
print("2.Fehrenheit to Celsius")
convert=int(input("Enter 1 or 2: "))
if convert==1:
    celsius=int(input("Enter celsius: "))
    print(c_to_f(celsius))
elif convert==2:
    fren=int(input("Enter Fehrenheit: "))
    print(f_to_c(fren))
else:
    print("Please Provide the Input properly")
