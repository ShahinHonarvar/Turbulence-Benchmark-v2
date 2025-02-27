def lists_with_product_equal_n(lst):
    n = 537
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == n:
                sublist = lst[i:j % len(lst)]
                sublists.append(sublist)
                break
            elif product > n:
                break
    return sublists