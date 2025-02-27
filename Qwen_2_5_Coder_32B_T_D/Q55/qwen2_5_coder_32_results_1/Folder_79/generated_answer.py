def lists_with_product_equal_n(circular_list):
    n = -83
    result = []
    len_list = len(circular_list)
    for start in range(len_list):
        product = 1
        for end in range(start, start + len_list):
            product *= circular_list[end % len_list]
            if product == n:
                result.append(circular_list[start:(end + 1) % len_list] if end < start + len_list else circular_list[start:] + circular_list[:end % len_list + 1])
    return result