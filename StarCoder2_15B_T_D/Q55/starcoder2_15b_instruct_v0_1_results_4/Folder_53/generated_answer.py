def lists_with_product_equal_n(lst):
    n = -87
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == 0 and j == len(lst):
                continue
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists