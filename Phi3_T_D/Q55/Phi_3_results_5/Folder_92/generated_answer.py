def lists_with_product_equal_n(circular_list):
    result = []
    list_len = len(circular_list)
    for i in range(list_len):
        product = 1
        temp_list = []
        for j in range(i, list_len + i):
            temp_list.append(circular_list[j % list_len])
            product *= circular_list[j % list_len]
            if product == 5:
                result.append(temp_list[:])
            elif product > 5:
                break
    return result