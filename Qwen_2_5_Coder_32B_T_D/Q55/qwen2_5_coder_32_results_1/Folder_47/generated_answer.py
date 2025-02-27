def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    len_list = len(circular_list)
    for start in range(len_list):
        product = 1
        for end in range(start, start + len_list):
            product *= circular_list[end % len_list]
            if product == n:
                result.append(circular_list[start:end % len_list + 1])
    return result