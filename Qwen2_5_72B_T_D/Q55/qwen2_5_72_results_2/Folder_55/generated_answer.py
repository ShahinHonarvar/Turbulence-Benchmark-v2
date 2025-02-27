def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == -6:
                result.append(sublist)
    result = [sub for sub in result if len(sub) <= n]
    return result