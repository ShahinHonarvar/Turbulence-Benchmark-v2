def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = lst[start:end % n]
            if product(sublist) == -15:
                result.append(sublist)
    return result