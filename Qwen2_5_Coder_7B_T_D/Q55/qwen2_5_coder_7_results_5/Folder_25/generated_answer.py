def lists_with_product_equal_n(lst):
    n = -32
    results = []
    n = abs(n)
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                results.append(lst[i:j + 1])
            elif product > n:
                break
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == n:
                results.append(lst[i:] + lst[:j + 1])
            elif product > n:
                break
    return results