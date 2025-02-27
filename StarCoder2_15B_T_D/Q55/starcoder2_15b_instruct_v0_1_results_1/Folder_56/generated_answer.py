def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i + 1, len(lst) + i):
            product *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if product == n:
                sublists.append(sublist)
                break
            elif product < 0 or product == 0:
                break
    return sublists