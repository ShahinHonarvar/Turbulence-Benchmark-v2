def lists_with_product_equal_n(circular_list):
    target_product = -23
    n = len(circular_list)
    result = []

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    for start in range(n):
        for end in range(n):
            sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == target_product:
                result.append(sublist)
    return result