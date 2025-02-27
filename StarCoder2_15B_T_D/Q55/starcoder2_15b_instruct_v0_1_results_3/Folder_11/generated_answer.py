def lists_with_product_equal_n(lst, n=-15):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) > len(lst):
                break
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == n:
                result.append(sublist)
    return result