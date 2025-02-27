def lists_with_product_equal_n(lst):
    n = -18
    sublists = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, i + len(lst)):
            sublist.append(lst[j % len(lst)])
            prod *= lst[j % len(lst)]
            if prod == n:
                sublists.append(sublist)
            elif prod < n:
                continue
            else:
                break
    return sublists