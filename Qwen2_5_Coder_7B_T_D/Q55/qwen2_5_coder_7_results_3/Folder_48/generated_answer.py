def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 990:
                result.append(lst[i:j % n + 1])
            elif product > 990:
                break
    return result