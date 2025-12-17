def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b!=0:
        return a / b
    else:
        return"Error:Division by zero"
import calculator

a= float(input("Enter first number: "))
b= float(input("Enter second number: "))

print("Addition: ",calculator.add(a,b))
print("Subtraction: ",calculator.subtract(a,b))
print("Multiplication: ",calculator.multiply(a,b))
print("Division: ",calculator.divide(a,b))
