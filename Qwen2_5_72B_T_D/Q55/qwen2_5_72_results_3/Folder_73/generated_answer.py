def lists_with_product_equal_n(circular_list):
    target_product = 40
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            product = 1
            for i in range(size):
                product *= circular_list[(start + i) % n]
            if product == target_product:
                result.append(circular_list[start:start + size])
                break
    return result