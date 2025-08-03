test_list = [0, 1, 7, 2, 4, 8]
final_result = 0
even_index_sum = 0
if not test_list:
    final_result = 0
else:
    for _ in range(0, len(test_list), 2):
        even_index_sum += test_list[_]
    final_result = even_index_sum * test_list[-1]
print(final_result)