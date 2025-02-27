def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= lst[end]
            if product == 36:
                sublist = lst[start:start + size]
                if start + size > n:
                    sublist += lst[:end]
                results.append(sublist)
            elif product > 36:
                break
    return results