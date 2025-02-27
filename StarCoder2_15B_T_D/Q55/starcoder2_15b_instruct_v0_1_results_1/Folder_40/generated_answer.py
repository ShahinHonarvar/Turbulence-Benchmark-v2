def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist_product = 1
            for k in range(i, j):
                k %= n
                sublist_product *= circular_list[k]
            if sublist_product == -9:
                result.append(circular_list[i:j])
    return result