def lists_with_product_equal_n(lst, n):
    result = []
    sublist = []
    product = 1
    for i in range(len(lst)):
        sublist.append(lst[i])
        product *= lst[i]
        while product > n and len(sublist) > 0:
            product //= sublist.pop(0)
        if product == n:
            result.append(sublist[:])
        if len(sublist) == 0:
            product = 1
            sublist = []
    return result