def lists_with_product_equal_n(lst):
    n = -83
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k % len(lst)]
            if prod == n:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(lst[k % len(lst)])
                sublists.append(sublist)
    return sublists