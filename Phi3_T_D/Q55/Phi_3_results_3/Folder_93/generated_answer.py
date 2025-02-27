def lists_with_product_equal_n(circular_list):
    target_product = 91
    n = len(circular_list)
    results = []

    def is_product_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for start in range(n):
        for size in range(1, n + 1):
            sublist = circular_list[start:start + size]
            if is_product_n(sublist):
                results.append(sublist)
    return results