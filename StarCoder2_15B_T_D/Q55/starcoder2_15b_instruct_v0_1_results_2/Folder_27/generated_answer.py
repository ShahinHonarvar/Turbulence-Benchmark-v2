def lists_with_product_equal_n(lst):
    n = -82
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j - 1:
                continue
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                continue
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                sublists.append(sublist)
    return sublists