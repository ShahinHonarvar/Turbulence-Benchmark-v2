def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            product *= circular_list[(start + size - 1) % n]
            if product == -8:
                results.append(circular_list[start:start + size])
    return results