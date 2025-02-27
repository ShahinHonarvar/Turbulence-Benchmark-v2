def lists_with_product_equal_n(circular_list):
    target_product = 990
    n = len(circular_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:] + circular_list[:end % n]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result