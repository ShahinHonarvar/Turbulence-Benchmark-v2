def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length - 1) % size
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end + 1])
                break
    return result