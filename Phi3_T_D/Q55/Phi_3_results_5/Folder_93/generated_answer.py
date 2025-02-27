def lists_with_product_equal_n(lst):
    n = -91
    size = len(lst)
    matches = []
    for i in range(size):
        prod = 1
        j = i
        sublist = []
        while prod != n:
            prod = prod * lst[j]
            sublist.append(lst[j])
            j = (j + 1) % size
            if prod == n or prod == 0 or lst[j] == 0:
                matches.append(sublist.copy())
                sublist.clear()
    return matches