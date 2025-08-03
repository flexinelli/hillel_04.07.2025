original_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

amount = original_list.count(0)

while 0 in original_list:
    original_list.remove(0)

for _ in range(amount):
    original_list.append(0)

print(original_list)