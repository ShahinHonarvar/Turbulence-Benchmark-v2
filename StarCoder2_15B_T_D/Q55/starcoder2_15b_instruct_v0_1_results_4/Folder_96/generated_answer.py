def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if len(sublist) <= n and all((x != 0 for x in sublist)):
                if 0 in sublist:
                    result.append(sublist)
            elif len(sublist) == n + 1 and 0 in sublist:
                result.append(sublist)
    return result