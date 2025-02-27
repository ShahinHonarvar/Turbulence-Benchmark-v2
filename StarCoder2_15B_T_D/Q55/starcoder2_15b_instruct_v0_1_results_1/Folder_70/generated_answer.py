def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (abs(sum([math.log2(x) for x in sublist]) - math.log2(n)) < 1e-06):
                sublists.append(sublist)
    return sublists