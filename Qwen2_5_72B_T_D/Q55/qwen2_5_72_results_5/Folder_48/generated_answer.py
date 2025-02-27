def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(n):
            sublist = circular_list[start:start + end + 1] if start + end + 1 <= n else circular_list[start:] + circular_list[:end + 1]
            if product(sublist) == 990:
                result.append(sublist)
    return result