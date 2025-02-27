def lists_with_product_equal_n(circular_list):
    n = -97
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        for sub_len in range(1, list_size + 1):
            sublist = []
            product = 1
            for j in range(sub_len):
                product *= circular_list[(i + j) % list_size]
                sublist.append(circular_list[(i + j) % list_size])
                if product == n and sublist not in result:
                    result.append(sublist[:])
    return result