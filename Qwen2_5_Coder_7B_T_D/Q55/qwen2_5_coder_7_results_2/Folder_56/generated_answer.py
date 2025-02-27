def lists_with_product_equal_n(lst):
    target = -65
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == target:
                result.append(lst[i:j % n])
    return result