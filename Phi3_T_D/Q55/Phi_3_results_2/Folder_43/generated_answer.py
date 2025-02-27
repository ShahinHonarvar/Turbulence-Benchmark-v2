def lists_with_product_equal_n(circular_list):
    result = []
    len_list = len(circular_list)
    for i in range(len_list):
        product = 1
        sublist = []
        for j in range(i, i + len_list):
            sublist.append(circular_list[j % len_list])
            product *= circular_list[j % len_list]
            if product == -26:
                result.append(sublist[:])
            elif product > -26:
                break
    return result