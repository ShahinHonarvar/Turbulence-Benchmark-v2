def lists_with_product_equal_n(lst):
    n = 15
    result = []
    size = len(lst)
    for i in range(size):
        prod = 1
        for j in range(i, size):
            prod *= lst[j]
            if prod == n:
                result.append(lst[i:j + 1])
            elif prod > n:
                break
    return result