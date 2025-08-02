def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2

from art import logo
print(logo)
num = int(input("What's the first number?: "))

def ask(num):
    print(f"+\n-\n*\n/")
    operation = input("Pick an operation: ")
    next_num = int(input("What's the next number?: "))
    result = 0
    if operation == "+":
        result = add(num, next_num)
    elif operation == "-":
        result = subtract(num, next_num)
    elif operation == "*":
        result = multiply(num, next_num)
    elif operation == "/":
        result = divide(num, next_num)
    else:
        print("Invalid inputs try again.")
        num = int(input("What's the first number?: "))
        ask(num)
    print(f"{num} {operation} {next_num} = {round(result, 2)}")
    again = input(f"Type 'y' to continue calculating with {round(result, 2)}, or type 'n' to start a new calculation: ").lower()
    if again == "n":
        print("\n"*10)
        print(logo)
        num = int(input("What's the first number?: "))
        ask(num)
    elif again == "y":
        ask(result)
ask(num)


