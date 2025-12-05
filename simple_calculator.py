def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: cannot divide by zero"
    return a / b


iterations = int(input("how many times do you want to calculate? "))

for i in range(iterations):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter the second number: "))
    op = input("enter operation (+, -, *, /): ")

    if op == "+":
        result = add(num1, num2)

    elif op == "-":
        result = subtract(num1, num2)

    elif op == "*":
        result = multiply(num1, num2)

    elif op == "/":
        result = divide(num1, num2)
        if result == "error: cannot divide by zero":
            print(result)
            continue

    else:
        print("invalid input")
        continue

    print("result:", result)