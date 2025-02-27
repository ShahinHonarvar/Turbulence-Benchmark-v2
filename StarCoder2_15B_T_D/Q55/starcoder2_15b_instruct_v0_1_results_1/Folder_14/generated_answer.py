def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
            if product == -72:
                sublists.append([lst[k % len(lst)] for k in range(i, j + 1)])
    return sublists