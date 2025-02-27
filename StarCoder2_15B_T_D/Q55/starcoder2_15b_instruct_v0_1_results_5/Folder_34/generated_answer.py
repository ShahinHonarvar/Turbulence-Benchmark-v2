def lists_with_product_equal_n(lst):
    n = -81
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k % len(lst)]
            if prod == n:
                result.append([lst[k % len(lst)] for k in range(i, j + 1)])
    return result