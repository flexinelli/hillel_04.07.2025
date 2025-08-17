print("")
print("Welcome to our calculator!")
print("")

while True:
    first_number = float(input("Enter the first number: "))

    while True:
        arithmetic_operation = input("Type the arithmetic operation you want to perform (+, -, *, /): ")
        if arithmetic_operation in ['+', '-', '*', '/']:
            break
        else:
            print("Error: Invalid operation. Please enter one of +, -, *, /.")

    second_number = float(input("Enter the second number: "))
    print("")

    if arithmetic_operation == "+":
        result = first_number + second_number
        print("Result:", result)

    elif arithmetic_operation == "-":
        result = first_number - second_number
        print("Result:", result)

    elif arithmetic_operation == "*":
        result = first_number * second_number
        print("Result:", result)

    elif arithmetic_operation == "/":
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = first_number / second_number
            print("Result:", result)

    print("")
    continue_calc = input("Do you want to continue?: ").lower()
    if continue_calc != "yes" and continue_calc != "y":
        print("Thanks for using our calculator!")
        break
    print("")