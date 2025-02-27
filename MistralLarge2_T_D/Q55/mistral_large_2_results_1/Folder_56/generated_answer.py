def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    res = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -65:
                res.append(circular_list[i:i + j + 1] if i + j + 1 <= n else circular_list[i:] + circular_list[:(i + j + 1) % n])
    return res