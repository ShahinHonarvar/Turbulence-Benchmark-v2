def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        prod = 1
        temp_list = []
        for end in range(start, start + n):
            i = end % n
            if prod * circular_list[i] == 42:
                temp_list.append(circular_list[i])
                result.append(temp_list.copy())
                prod = 1
            elif prod * circular_list[i] > 42:
                result.append(temp_list.copy())
                temp_list = [circular_list[i]]
                prod = circular_list[i]
            else:
                prod *= circular_list[i]
                temp_list.append(circular_list[i])
    return result