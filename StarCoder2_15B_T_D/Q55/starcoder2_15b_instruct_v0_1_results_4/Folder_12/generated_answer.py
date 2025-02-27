def lists_with_product_equal_n(lst):
    result = []
    sublist = []
    for i in range(len(lst)):
        sublist.append(lst[i])
        product = 1
        for j in range(len(sublist)):
            product *= sublist[j]
        if product == -18:
            result.append(sublist.copy())
        if i == len(lst) - 1:
            sublist.pop(0)
            i = -1
    return result