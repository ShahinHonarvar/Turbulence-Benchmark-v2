def lists_with_product_equal_n(circular_list):
    n = -20
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            index = end % size
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:index + 1])
    return result