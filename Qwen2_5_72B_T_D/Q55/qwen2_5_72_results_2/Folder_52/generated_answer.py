def lists_with_product_equal_n(circular_list):
    target_product = 37
    n = len(circular_list)
    result = []

    def check_sublist(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % n]
        return product == target_product
    for start in range(n):
        for length in range(1, n + 1):
            if check_sublist(start, length):
                sublist = circular_list[start:start + length]
                if length > 1 and start + length > n:
                    sublist = circular_list[start:] + circular_list[:start + length - n]
                result.append(sublist)
    return result