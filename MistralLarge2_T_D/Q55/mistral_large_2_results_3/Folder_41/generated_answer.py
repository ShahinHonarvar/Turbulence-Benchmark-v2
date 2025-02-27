def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            for i in range(start, start + size):
                product *= circular_list[i % n]
            if product == -20:
                results.append([circular_list[(start + j) % n] for j in range(size)])
            product = 1
    return results