def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        product = 1
        for i in range(start, list_length):
            product *= circular_list[i]
            if product == n:
                result.append(circular_list[start:i + 1])
            elif product > n:
                break
    return result