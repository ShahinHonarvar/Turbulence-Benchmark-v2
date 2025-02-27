def lists_with_product_equal_n(lst):
    n = 53
    result = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, lst_len + i):
            product *= lst[j % lst_len]
            if product == n:
                result.append(lst[i:j % lst_len])
            elif product > n:
                break
    return result