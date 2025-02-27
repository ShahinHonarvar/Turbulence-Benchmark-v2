def lists_with_product_equal_n(lst):
    n = -97
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and len(sublist) > 0:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    sublists.append(sublist)
    return sublists