def lists_with_product_equal_n(lst):
    n = 85
    result = []
    length = len(lst)
    for i in range(length):
        prod = 1
        for j in range(i, length + i):
            prod *= lst[j % length]
            if prod == n:
                result.append(lst[i:j % length + 1])
            elif prod > n:
                break
    return result