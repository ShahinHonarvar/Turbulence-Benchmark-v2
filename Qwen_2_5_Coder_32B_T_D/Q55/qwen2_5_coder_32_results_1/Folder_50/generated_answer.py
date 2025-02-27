def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, n + start + 1):
            end %= n
            sublist = lst[start:end] if end >= start else lst[start:] + lst[:end]
            if product(sublist) == 45:
                result.append(sublist)
    return result