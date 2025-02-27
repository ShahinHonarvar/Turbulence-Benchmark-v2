def lists_with_product_equal_n(lst):
    sublists = []
    n = -83
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                sublists.append(sublist)
    return sublists