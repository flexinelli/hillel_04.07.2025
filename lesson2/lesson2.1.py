number = int(input("Enter FOUR digits:"))

num1 = number // 1000
num2 = number % 1000 // 100
num3 = number % 1000 // 10 % 10
num4 = number % 1000 % 10

print(num1)
print(num2)
print(num3)
print(num4)