def lists_with_product_equal_n(circular_list):
    n = -41
    result = []
    l = len(circular_list)
    for start in range(l):
        product = 1
        for end in range(start, start + l):
            product *= circular_list[end % l]
            if product == n:
                result.append(circular_list[start:end % l + 1])
    return result