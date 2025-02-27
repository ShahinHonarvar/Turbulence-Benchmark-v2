def lists_with_product_equal_n(circular_list):
    target_product = -83
    n = len(circular_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(2 * n):
        for end in range(start + 1, 2 * n + 1):
            sublist = circular_list[start % n:end % n]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result