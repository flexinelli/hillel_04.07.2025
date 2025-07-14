number = int(input("Enter FIVE digits:"))

num1 = number // 10000
num2 = number // 1000 % 10
num3 = number % 1000 // 100
num4 = number % 1000 // 10 % 10
num5 = number % 1000 % 10

print(num5 * 10000 + num4 * 1000 + num3 * 100 + num2 * 10 + num1)