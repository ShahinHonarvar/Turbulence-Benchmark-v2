def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    if len_list == 0:
        return []
    result = []
    for i in range(len(circular_list)):
        prod, temp_list = (1, [])
        for j in range(i, i + len_list):
            temp_list.append(circular_list[j % len_list])
            prod *= circular_list[j % len_list]
            if prod == 3:
                result.append(temp_list)
                break
            elif prod > 3:
                break
    return result