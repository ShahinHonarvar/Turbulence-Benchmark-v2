def lists_with_product_equal_n(lst):
    n = -6
    results = []
    for i in range(len(lst)):
        total = 1
        for j in range(i, len(lst) + i):
            total *= lst[j % len(lst)]
            if total == n:
                results.append(lst[i:j % len(lst) + 1])
            elif total > n:
                break
    return results