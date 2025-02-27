def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k % len(lst)]
            if prod == -6:
                sublists.append([lst[k % len(lst)] for k in range(i, j + 1)])
    return sublists