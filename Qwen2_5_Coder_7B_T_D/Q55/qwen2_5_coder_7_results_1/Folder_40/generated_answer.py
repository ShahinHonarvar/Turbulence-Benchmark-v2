def lists_with_product_equal_n(circular_list):
    n = -9
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, length + start):
            product *= circular_list[end % length]
            if product == n:
                result.append(circular_list[start:end % length])
    return result