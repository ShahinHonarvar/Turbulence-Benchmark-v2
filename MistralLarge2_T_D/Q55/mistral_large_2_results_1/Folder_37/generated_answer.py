def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= circular_list[end]
            if product == -76:
                result.append(circular_list[start:start + length] if start + length <= n else circular_list[start:] + circular_list[:end + 1])
    return result