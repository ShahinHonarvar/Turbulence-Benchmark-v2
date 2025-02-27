def lists_with_product_equal_n(lst):
    n = 48
    result = []
    length = len(lst)
    for i in range(length):
        prod = 1
        for j in range(i, length):
            prod *= lst[j]
            if prod == n:
                result.append(lst[i:j + 1])
            elif prod > n:
                break
    return result