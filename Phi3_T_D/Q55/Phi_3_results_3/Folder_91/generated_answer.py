def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    results = []
    for i in range(length):
        for j in range(i, length):
            if circular_list[i] == 2:
                sublist = circular_list[i:j + 1]
                if sublist.count(2) > 1:
                    results.append(sublist)
    circular_start = results.copy()
    for start_index in range(length):
        sublist = []
        for end_index in range(start_index, length + start_index):
            value = circular_list[end_index % length]
            if value == 2:
                sublist.append(value)
                if sublist.count(2) > 1:
                    circular_start.append(sublist.copy())
            else:
                sublist.clear()
    return circular_start