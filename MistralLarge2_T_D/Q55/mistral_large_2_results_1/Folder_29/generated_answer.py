def lists_with_product_equal_n(lst, n=15):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    result = []
    size = len(lst)
    lst = lst + lst
    for start in range(size):
        for length in range(1, size + 1):
            sublist = lst[start:start + length]
            if product(sublist) == n:
                result.append(sublist)
    return result