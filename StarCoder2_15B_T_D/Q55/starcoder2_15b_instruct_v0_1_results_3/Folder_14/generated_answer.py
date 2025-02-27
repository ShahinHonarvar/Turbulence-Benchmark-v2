def lists_with_product_equal_n(lst, n=-72):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + i):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) > 0 and len(sublist) <= len(lst) and (1 in sublist):
                if len(sublist) == 1:
                    if sublist[0] == n:
                        result.append(sublist)
                elif n % sublist[0] == 0:
                    if sublist[0] * n // sublist[0] == n:
                        result.append(sublist)
    return result