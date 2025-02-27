def lists_with_product_equal_n(lst):
    n = -115
    sublists = []
    for i in range(len(lst)):
        current_product = 1
        current_sublist = []
        for j in range(i, i + len(lst)):
            current_product *= lst[j % len(lst)]
            current_sublist.append(lst[j % len(lst)])
            if current_product == n:
                sublists.append(current_sublist)
                break
    return sublists