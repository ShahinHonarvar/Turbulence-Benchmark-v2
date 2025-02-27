def lists_with_product_equal_n(lst):
    n = -23
    result = []
    n_len = len(lst)
    for i in range(n_len):
        prod = 1
        for j in range(i, n_len + i):
            prod *= lst[j % n_len]
            if prod == n:
                result.append(lst[i:j % n_len + 1])
            elif prod > n:
                break
    return result