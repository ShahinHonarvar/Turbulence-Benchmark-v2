def lists_with_product_equal_n(circular_list):
    n = 13
    result = []
    list_len = len(circular_list)
    for i in range(list_len):
        product = 1
        for j in range(i, list_len + i):
            product *= circular_list[j % list_len]
            if product == n:
                result.append(circular_list[i:j % list_len])
            elif product > n:
                break
    return result