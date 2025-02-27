def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= circular_list[end]
            if product == 57:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            elif product > 57:
                break
    return result