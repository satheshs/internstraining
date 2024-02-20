def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
a=int(input("Enter the Number 1:"))
b=int(input("Enter the Number 2:"))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
operaion=int(input("Please Enter any of the number to perfrom the following Operation:"))
if operaion==1:
    print(add(a,b))
elif operaion==2:
    print(sub(a,b))
elif operaion==3:
    print(mul(a,b))
elif operaion==4:
    print(div(a,b))