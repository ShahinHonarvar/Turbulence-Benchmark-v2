def lists_with_product_equal_n(circular_list):
    n = 32
    result = []
    n_len = len(circular_list)
    for i in range(n_len):
        product = 1
        for j in range(i, n_len + i):
            product *= circular_list[j % n_len]
            if product == n:
                result.append(circular_list[i:j % n_len])
            elif product > n:
                break
    return result