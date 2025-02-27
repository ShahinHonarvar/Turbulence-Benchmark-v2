def lists_with_product_equal_n(lst):
    n = -22
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst):
                if len(sublist) > 1:
                    product = 1
                    for num in sublist:
                        product *= num
                else:
                    product = sublist[0]
                if product == n:
                    sublists.append(sublist)
    return sublists