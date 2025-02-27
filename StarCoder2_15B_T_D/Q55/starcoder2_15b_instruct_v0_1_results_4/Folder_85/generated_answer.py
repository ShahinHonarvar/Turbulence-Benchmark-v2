def lists_with_product_equal_n(lst):
    n = -97
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if lst[i:j]:
                if n == 1:
                    sublists.extend([lst[i:j]] * len(lst))
                elif n == 0:
                    sublists.append(lst[i:j])
                else:
                    prod = 1
                    for k in lst[i:j]:
                        prod *= k
                    if prod == n:
                        sublists.append(lst[i:j])
    return sublists