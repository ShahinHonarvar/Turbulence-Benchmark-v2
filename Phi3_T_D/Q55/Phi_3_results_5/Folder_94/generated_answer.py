def lists_with_product_equal_n(circular_list):
    result = []
    list_len = len(circular_list)
    circular_list += circular_list[:list_len - 1]
    for size in range(1, list_len + 1):
        for i in range(0, list_len):
            product = 1
            sublist = []
            for j in range(i, i + size):
                sublist.append(circular_list[j])
                product *= circular_list[j]
            if product == -30:
                sublist *= -1 if sublist[0] < 0 else 1
                result.append(sublist)
    return result