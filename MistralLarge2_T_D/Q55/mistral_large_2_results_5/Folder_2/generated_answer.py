def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == -968:
                sublist = circular_list[start:start + length]
                if start + length > n:
                    sublist += circular_list[:(start + length) % n]
                result.append(sublist)
    return result