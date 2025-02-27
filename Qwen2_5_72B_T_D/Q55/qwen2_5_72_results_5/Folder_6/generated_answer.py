def lists_with_product_equal_n(circular_list):
    n = 42
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length) % size
            product *= circular_list[start]
            if product == n:
                result.append(circular_list[start:end] if start < end else circular_list[start:] + circular_list[:end])
            if end != start:
                product //= circular_list[end]
    return result