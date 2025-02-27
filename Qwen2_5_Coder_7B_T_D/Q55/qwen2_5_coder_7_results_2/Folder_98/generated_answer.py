def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j % n]
            if product == -1:
                result.append(lst[i:j + 1])
            elif product > -1:
                break
    return result