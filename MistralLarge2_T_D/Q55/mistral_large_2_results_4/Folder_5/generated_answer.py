def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= circular_list[end]
            if product == -33:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                results.append(sublist)
            if product == 0:
                break
    return results