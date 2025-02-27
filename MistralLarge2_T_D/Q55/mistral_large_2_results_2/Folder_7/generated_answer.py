def lists_with_product_equal_n(circular_list):
    n = 537
    size = len(circular_list)
    result = []

    def check_sublist(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % size]
        if product == n:
            result.append(circular_list[start:start + length])
    for length in range(1, size + 1):
        for start in range(size):
            check_sublist(start, length)
    return result