def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublist(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % n]
        return product
    for start in range(n):
        for length in range(1, n + 1):
            if check_sublist(start, length) == -938:
                result.append([circular_list[(start + i) % n] for i in range(length)])
    return result