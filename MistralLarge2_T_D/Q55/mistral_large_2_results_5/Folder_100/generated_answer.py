def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublist(start, size):
        product = 1
        for i in range(size):
            product *= circular_list[(start + i) % n]
        return product == 48
    for start in range(n):
        for size in range(1, n + 1):
            if check_sublist(start, size):
                sublist = [circular_list[(start + i) % n] for i in range(size)]
                result.append(sublist)
    return result