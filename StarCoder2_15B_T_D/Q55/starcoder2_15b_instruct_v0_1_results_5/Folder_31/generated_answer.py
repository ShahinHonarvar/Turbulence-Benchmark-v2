def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        sublist = []
        product = 1
        for j in range(i, i + len(lst)):
            sublist.append(lst[j % len(lst)])
            product *= lst[j % len(lst)]
            if product == n:
                sublists.append(sublist)
            elif product < 0:
                break
    return sublists