def lists_with_product_equal_n(lst):
    n = -690
    result = []
    n_len = len(lst)
    for i in range(n_len):
        product = 1
        for j in range(i, n_len):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return result