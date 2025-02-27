def lists_with_product_equal_n(circular_list):
    n = -75
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            index = end % size
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:index + 1])
    return result