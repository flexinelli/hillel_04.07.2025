print("")
print("Welcome to our calculator!")
print("")
first_number = float(input("Enter the first number: "))

arithmetic_operation = input("Type the arithmetic operation you want to perform: ")
if arithmetic_operation not in ['+', '-', '*', '/']:
    print("")
    print("Error: Invalid operation. Please enter one of +, -, *, /.")
    arithmetic_operation = input("Try again! Type the arithmetic operation you want to perform:")
    print("")

second_number = float(input("Enter the second number: "))

print("")

if arithmetic_operation == "+":
    if arithmetic_operation == "+" and (first_number + second_number) % 1 == 0:
        result = first_number + second_number
        print(int(result))
    else:
        result = first_number + second_number
        print(result)

elif arithmetic_operation == "-":
    if arithmetic_operation == "-" and (first_number - second_number) % 1 == 0:
        result = first_number - second_number
        print(int(result))
    else:
        result = first_number - second_number
        print(result)

elif arithmetic_operation == "*":
    if arithmetic_operation == "*" and (first_number * second_number) % 1 == 0:
        result = first_number * second_number
        print(int(result))
    else:
        result = first_number * second_number
        print(result)

elif arithmetic_operation == "/" and second_number != 0 and first_number % second_number == 0:
    result = first_number / second_number
    print(int(result))
elif arithmetic_operation == "/" and second_number != 0:
    result = first_number / second_number
    print(result)
else:
    print("Error: Division by zero is not allowed.")
    second_number = float(input("Enter the second number: "))
    if second_number == 0:
        print("")
        print("Sorry! You've reached the limit of free attempts to divide by zero.")
    elif arithmetic_operation == "/" and second_number != 0 and first_number % second_number == 0:
        result = first_number / second_number
        print(int(result))
    elif arithmetic_operation == "/" and second_number != 0:
        result = first_number / second_number
        print(result)

print("")
print("To continue using our calculator, please subscribe to the premium plan.")
bank_details_scam_try = input("Enter your bank details (100% safe, trust us): ")