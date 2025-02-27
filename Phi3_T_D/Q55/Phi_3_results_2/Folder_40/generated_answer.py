def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list += circular_list
    for i in range(1, len(circular_list) - n + 1):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
        if product == -9:
            result.append(circular_list[i:i + n])
    return result