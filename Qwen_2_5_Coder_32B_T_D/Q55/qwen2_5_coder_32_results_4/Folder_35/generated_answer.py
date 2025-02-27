def lists_with_product_equal_n(lst):
    n = 83
    result = []
    l = len(lst)
    for i in range(l):
        product = 1
        for j in range(i, i + l):
            product *= lst[j % l]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return result