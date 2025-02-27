def lists_with_product_equal_n(lst):
    n = -30
    sublists = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        product = lst[i]
        j = (i + 1) % len(lst)
        while j != i:
            sublist.append(lst[j])
            product *= lst[j]
            if product == n:
                sublists.append(sublist)
            j = (j + 1) % len(lst)
    return sublists