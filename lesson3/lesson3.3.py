lst = [111, 222, 333, 444, 555, 666, 777]
if len(lst) % 2 == 0:
    slice_midpoint = int(len(lst) / 2)
    first_list = lst[:slice_midpoint:]
    second_list = lst[slice_midpoint:]
    my_list = []
    my_list.append(first_list)
    my_list.append(second_list)
    print(my_list)
else:
    slice_midpoint = int(len(lst) // 2)
    slice_midpoint = slice_midpoint + 1
    first_list = lst[:slice_midpoint:]
    second_list = lst[slice_midpoint:]
    my_list = []
    my_list.append(first_list)
    my_list.append(second_list)
    print(my_list)