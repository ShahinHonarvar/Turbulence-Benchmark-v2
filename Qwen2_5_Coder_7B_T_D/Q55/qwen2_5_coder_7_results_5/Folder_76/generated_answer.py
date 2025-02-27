def lists_with_product_equal_n(lst):
    n = 247
    result = []
    n_len = len(lst)
    for i in range(n_len):
        product = 1
        for j in range(i, n_len + i):
            product *= lst[j % n_len]
            if product == n:
                result.append(lst[i:j % n_len + 1])
            elif product > n:
                break
    return result