def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_sublist_product(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % n]
        return product
    for start in range(n):
        for length in range(1, n + 1):
            if get_sublist_product(start, length) == -968:
                result.append(circular_list[start:start + length])
    return result