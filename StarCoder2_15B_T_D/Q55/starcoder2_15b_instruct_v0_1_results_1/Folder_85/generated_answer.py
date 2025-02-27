def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if len(sublist) <= n and prod(sublist) == -97:
                sublists.append(sublist)
    return sublists

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p