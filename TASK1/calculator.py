# Python Calculator Program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is undefined"
    return x / y

def calculator():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Type 'stop' to exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'stop': ").lower()

        if choice == 'stop':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

            
            continue_or_stop = input("\nDo you want to perform another operation? (yes to continue, 'stop' to exit): ").lower()

            if continue_or_stop == 'stop':
                print("Exiting the calculator.")
                break
        else:
            print("Invalid input. Please enter a valid option.")


calculator()
