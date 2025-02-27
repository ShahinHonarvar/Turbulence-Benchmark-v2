def lists_with_product_equal_n(circular_list):
    n = -83
    size = len(circular_list)
    results = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length - 1) % size
            product *= circular_list[end]
            if product == n:
                results.append(circular_list[start:start + length])
            if product == 0:
                break
    return results