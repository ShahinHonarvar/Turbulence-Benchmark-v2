def lists_with_product_equal_n(lst):
    result = []
    n = -115
    length = len(lst)
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, length + i):
            product *= lst[j % length]
            sublist.append(lst[j % length])
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result