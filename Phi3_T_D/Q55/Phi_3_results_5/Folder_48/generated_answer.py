def lists_with_product_equal_n(circular_list):
    target_product = 990
    results = []

    def check_sublist(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[start + i]
        return product == target_product
    for length in range(1, len(circular_list) + 1):
        for start in range(len(circular_list)):
            if check_sublist(start, length):
                results.append(circular_list[start:start + length])
    return results