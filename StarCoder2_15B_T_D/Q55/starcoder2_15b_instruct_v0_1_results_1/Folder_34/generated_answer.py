def lists_with_product_equal_n(lst):
    n = -81
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist_product = 1
            for k in range(i, j):
                sublist_product *= lst[k % len(lst)]
            if sublist_product == n:
                sublists.append(lst[i:j])
    return sublists