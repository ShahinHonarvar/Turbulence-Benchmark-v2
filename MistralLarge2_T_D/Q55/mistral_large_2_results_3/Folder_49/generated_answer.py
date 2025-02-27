def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product_target = -61
    result = []

    def check_sublist(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i % n]
        return product == product_target
    for size in range(1, n + 1):
        for i in range(n):
            if check_sublist(i, i + size - 1):
                result.append(circular_list[i:i + size])
    return result