

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    import art
    print(art.logo)
    should_continue = True
    num1 = int(input("Enter first number: "))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        num2 = int(input("Enter second number: "))
        answer =operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' if you want to continue {answer} or 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_continue = False
            print("\n" *20)
            calculator()
calculator()
