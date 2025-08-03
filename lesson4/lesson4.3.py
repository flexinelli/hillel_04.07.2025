import random
test_list = [random.randint(0, 10) for _ in range(random.randint(3, 10))]
print("Random list:",test_list)
result = []
if len(test_list) > 3:
    result = [test_list[0], test_list[2], test_list[-2]]
else:
    result = [test_list[0], test_list[2], test_list[1]]

print(result)