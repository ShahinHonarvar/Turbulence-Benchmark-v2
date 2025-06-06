def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == 8:
                result.append(circular_list[start:end + 1] if end < n else circular_list[start:] + circular_list[:end % n + 1])
    return result