def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k % len(lst)]
            if prod == n:
                sublists.append(lst[i:j + 1])
    return sublists