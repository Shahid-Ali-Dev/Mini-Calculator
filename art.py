logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
print(logo)
dictionary = {"+" : add ,  "*" : multiply ,  "-" : subtract ,  "/" : divide}
num = float(input("What's the first number?: "))
def ask(num):
    print(f"+\n-\n*\n/")
    operation = input("Pick an operation: ")
    if operation not in dictionary:
        print("Invalid operation, Try again")
        ask(num)
    next_num = float(input("What's the next number?: "))
    result = dictionary.get(operation)(num, next_num)
    print(f"{round(num,2)} {operation} {next_num} = {round(result, 2)}")
    again = input(
        f"Type 'y' to continue calculating with {round(result, 2)}, or type 'n' to start a new calculation: ").lower()
    if again == "y":
        ask(result)
    else:
        print(logo)
        print("\n"*10)
        num = float(input("What's the first number?: "))
        ask(num)

ask(num)

