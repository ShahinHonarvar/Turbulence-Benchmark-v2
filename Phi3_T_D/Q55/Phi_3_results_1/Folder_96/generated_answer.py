def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    found = False
    for size in range(1, n + 1):
        i = 0
        while i + size <= n:
            sub = lst[i:i + size]
            if 0 in sub:
                results.append(sub)
                found = True
            i += 1
            if i + size > n:
                i = n - size
    return results or []