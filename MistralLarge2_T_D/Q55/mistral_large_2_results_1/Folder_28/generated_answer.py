def lists_with_product_equal_n(circular_list):
    n = 85
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length) % size
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:start + length] if start + length <= size else circular_list[start:] + circular_list[:end])
            elif product > n:
                break
    return result