def lists_with_product_equal_n(lst, n):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            sublist = lst[i:j + 1]
            if len(sublist) > len(lst):
                continue
            if len(sublist) == len(lst) and sublist[0] != lst[-1]:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                yield sublist