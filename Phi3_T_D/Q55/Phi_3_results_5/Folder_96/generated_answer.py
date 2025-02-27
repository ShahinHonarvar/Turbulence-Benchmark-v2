def lists_with_product_equal_n(circular_list):
    circular_list += circular_list[:-1]
    length = len(circular_list)
    zero_indices = [i for i, x in enumerate(circular_list) if x == 0]
    result = []
    for start in zero_indices:
        temp_list = circular_list[start:] + circular_list[:start]
        for i in range(length):
            for j in range(i + 1, length + 1):
                sublist = temp_list[i:j]
                if any((x == 0 for x in sublist)):
                    result.append(sublist)
    if circular_list[0] == 0:
        circular_list = circular_list[1:] + [circular_list[0]]
        for start in zero_indices:
            temp_list = circular_list[start:] + circular_list[:start]
            for i in range(length):
                for j in range(i + 1, length + 1):
                    sublist = temp_list[i:j]
                    if any((x == 0 for x in sublist)):
                        result.append(sublist)
    return result