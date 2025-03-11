# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("Simple Calculator")
print("Operations available: +, -, *, /")

while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator")

    again = input("Calculate again? (y/n): ")
    if again.lower() != 'y':
        break
