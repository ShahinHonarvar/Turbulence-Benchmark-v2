def lists_with_product_equal_n(lst):
    if any((n < 0 for n in lst)):
        return []
    target = 46
    sublists = []
    n = len(lst)
    for size in range(1, n + 1):
        for start in range(n):
            end = (start + size) % n
            if lst[start] * lst[end % n] < target:
                continue
            if lst[start] * lst[end % n] == target:
                sublist = lst[start:end % n + 1]
                sublists.append(sublist)
    return sublists