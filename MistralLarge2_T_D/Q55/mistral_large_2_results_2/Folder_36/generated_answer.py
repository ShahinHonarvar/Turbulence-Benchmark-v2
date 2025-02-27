def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_sublist(start, end):
        product = 1
        for i in range(start, end):
            product *= circular_list[i % n]
        return product == 714
    for size in range(1, n + 1):
        for start in range(n):
            if check_sublist(start, start + size):
                result.append(circular_list[start:start + size])
    return result