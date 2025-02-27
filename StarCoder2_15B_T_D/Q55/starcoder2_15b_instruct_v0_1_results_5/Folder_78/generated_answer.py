def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, i + n):
            sublist = lst[i:j]
            if len(sublist) <= n and product(sublist) == 74:
                result.append(sublist)
    return result

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p