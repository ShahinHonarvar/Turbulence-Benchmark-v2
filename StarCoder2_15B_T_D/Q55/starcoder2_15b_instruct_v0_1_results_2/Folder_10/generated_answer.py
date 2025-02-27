def lists_with_product_equal_n(lst):
    n = -93
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
            if product == n:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(lst[k % len(lst)])
                sublists.append(sublist)
    return sublists