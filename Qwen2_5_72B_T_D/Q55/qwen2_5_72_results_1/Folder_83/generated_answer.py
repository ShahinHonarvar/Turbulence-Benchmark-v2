def lists_with_product_equal_n(circular_list):
    target_product = -57
    n = len(circular_list)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:] + circular_list[:end % n]
            if product(sublist) == target_product:
                result.append(sublist)
    return result