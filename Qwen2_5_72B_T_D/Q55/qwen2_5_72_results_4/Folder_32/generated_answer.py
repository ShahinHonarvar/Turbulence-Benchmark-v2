def lists_with_product_equal_n(circular_list):
    n = 76
    length = len(circular_list)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for start in range(length):
        for end in range(1, length + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == n:
                result.append(sublist)
    return result