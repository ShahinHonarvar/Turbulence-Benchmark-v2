def lists_with_product_equal_n(lst):
    n = -20
    if len(lst) == 0:
        return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if 1 in lst[i:j] and 0 in lst[i:j]:
                continue
            if 0 in lst[i:j]:
                product = 1
            else:
                product = 0
            for k in lst[i:j]:
                product *= k
            if product == n:
                sublists.append(lst[i:j])
    return sublists