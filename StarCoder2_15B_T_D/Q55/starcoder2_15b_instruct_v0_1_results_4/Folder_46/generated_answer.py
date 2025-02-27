def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if len(sublist) <= n and 53 % prod(sublist) == 0:
                result.append(sublist)
    return result

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p