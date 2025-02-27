def lists_with_product_equal_n(circular_list):
    n = -89
    result = []
    for i in range(len(circular_list)):
        prod = 1
        sublist = []
        for j in range(len(circular_list)):
            current_index = (i + j) % len(circular_list)
            prod *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if prod == n:
                result.append(sublist.copy())
            if prod != 0 and circular_list[current_index] == 0:
                break
    return result