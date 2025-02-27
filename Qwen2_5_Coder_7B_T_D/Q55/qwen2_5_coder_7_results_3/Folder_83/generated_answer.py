def lists_with_product_equal_n(lst):
    n = -57
    result = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, lst_len * 2):
            product *= lst[j % lst_len]
            if product == n:
                result.append(lst[i:j % lst_len])
            elif product > n:
                break
    return result