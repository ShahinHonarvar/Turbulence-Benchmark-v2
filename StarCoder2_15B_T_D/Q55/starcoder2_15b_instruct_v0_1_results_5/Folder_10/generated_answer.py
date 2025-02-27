def lists_with_product_equal_n(lst):
    n = -93
    res = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            sublist.append(lst[index])
            prod *= lst[index]
            if prod == n:
                res.append(sublist)
            elif prod > n or prod == 0:
                break
    return res