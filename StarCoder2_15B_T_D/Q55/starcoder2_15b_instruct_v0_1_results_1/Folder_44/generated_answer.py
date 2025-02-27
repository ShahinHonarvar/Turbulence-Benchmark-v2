def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        current_prod = 1
        current_sublist = []
        for j in range(i, i + len(lst)):
            current_sublist.append(lst[j % len(lst)])
            current_prod *= lst[j % len(lst)]
            if current_prod == n:
                sublists.append(current_sublist)
            if current_prod > n:
                break
    return sublists