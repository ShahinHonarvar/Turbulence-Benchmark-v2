def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) < length:
                sublist += circular_list[:length - len(sublist)]
            if get_product(sublist) == 632:
                result.append(sublist)
    return result