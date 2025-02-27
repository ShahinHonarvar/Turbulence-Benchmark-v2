def lists_with_product_equal_n(circular_list):
    n = -23
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end % size]
            if product == n:
                result.append(circular_list[start:end % size + 1])
    return result