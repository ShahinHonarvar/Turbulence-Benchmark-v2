def lists_with_product_equal_n(lst):
    n = 733
    sublists = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                sublists.append(sublist)
                break
            elif product > n:
                break
    return sublists