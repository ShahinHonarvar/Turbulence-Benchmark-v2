def lists_with_product_equal_n(circular_list):
    n = -7
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            product = 1
            for k in range(i, j):
                product *= circular_list[k % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j])
    return result