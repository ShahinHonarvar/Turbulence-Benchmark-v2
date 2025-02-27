def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            for k in range(j, len(lst)):
                if lst[(i + 1) % len(lst)] * lst[(j + 1) % len(lst)] * lst[(k + 1) % len(lst)] == n:
                    sublists.append([lst[(i + 1) % len(lst)], lst[(j + 1) % len(lst)], lst[(k + 1) % len(lst)]])
    return sublists