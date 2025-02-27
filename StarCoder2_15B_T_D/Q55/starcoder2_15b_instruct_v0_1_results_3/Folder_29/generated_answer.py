def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for window_size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(i, i + window_size):
                product *= circular_list[j % n]
            if product == 15:
                result.append(circular_list[i:i + window_size])
    return result