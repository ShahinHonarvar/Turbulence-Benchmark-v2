def lists_with_product_equal_n(circular_list):
    n = -81
    length = len(circular_list)
    result = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j % length]
            if product == n:
                result.append(circular_list[i:j % length + 1])
    return result