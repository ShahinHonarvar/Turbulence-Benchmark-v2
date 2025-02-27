def lists_with_product_equal_n(lst):
    n = -97
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
            if product == n:
                sublist = [lst[k % len(lst)] for k in range(i, j + 1)]
                sublists.append(sublist)
    return sublists