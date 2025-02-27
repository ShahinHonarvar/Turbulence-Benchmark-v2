def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = lst[i:j % n]
            if product(sublist) == 29:
                result.append(sublist)
    return result