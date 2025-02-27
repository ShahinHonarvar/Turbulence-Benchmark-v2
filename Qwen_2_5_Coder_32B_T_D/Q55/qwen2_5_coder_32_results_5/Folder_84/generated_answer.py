def lists_with_product_equal_n(circular_list):
    n = -906
    length = len(circular_list)
    results = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n:
                results.append(circular_list[start % length:end % length + 1])
    return results