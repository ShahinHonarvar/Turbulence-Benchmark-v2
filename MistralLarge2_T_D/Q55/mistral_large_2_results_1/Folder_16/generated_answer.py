def lists_with_product_equal_n(circular_list):
    n = -837
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            product *= circular_list[(start + length - 1) % size]
            if product == n:
                result.append(circular_list[start:start + length])
            if product == 0:
                break
    return result