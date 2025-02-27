def lists_with_product_equal_n(lst):

    def is_product_negative_115(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -115
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublist = lst[start:end]
            if is_product_negative_115(sublist):
                result.append(sublist)
    return result