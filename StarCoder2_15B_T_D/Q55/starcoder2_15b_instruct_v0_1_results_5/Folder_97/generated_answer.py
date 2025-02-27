def lists_with_product_equal_n(lst):
    n = -938
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and len(sublist) > 0 and (n % sublist[0] == 0) and (n / sublist[0] == 1):
                result.append(sublist)
    return result