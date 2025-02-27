def lists_with_product_equal_n(lst):
    result = []
    n = -57
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            if prod == n:
                result.append(lst[i:j % len(lst) + 1])
                break
            elif prod > n:
                break
    return result