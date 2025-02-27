def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j] + circular_list[:max(j - n, 0)]
            if product(sublist) == 29:
                result.append(sublist)
    return result