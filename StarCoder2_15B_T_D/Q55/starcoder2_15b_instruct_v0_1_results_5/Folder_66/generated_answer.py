def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i != j and i != j - 1:
                sublist = lst[i:j]
                if len(sublist) <= len(lst) and len(sublist) > 0:
                    product = 1
                    for k in range(len(sublist)):
                        product *= sublist[k]
                    if product == n:
                        result.append(sublist)
    return result