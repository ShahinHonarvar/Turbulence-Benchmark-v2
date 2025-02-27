def lists_with_product_equal_n(circular_list):
    n = 57
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            current_index = j % len(circular_list)
            current_product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if current_product == n:
                result.append(sublist.copy())
                break
            elif current_product > n:
                break
    return result