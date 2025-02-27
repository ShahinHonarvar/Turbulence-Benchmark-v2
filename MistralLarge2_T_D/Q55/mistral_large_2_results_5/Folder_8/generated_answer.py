def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            product *= circular_list[(start + size - 1) % n]
            if product == -41:
                result.append(circular_list[start:start + size])
                product = 1
    return result