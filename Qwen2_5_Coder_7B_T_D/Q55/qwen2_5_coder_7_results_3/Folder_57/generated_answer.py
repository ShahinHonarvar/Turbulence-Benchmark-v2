def lists_with_product_equal_n(lst):
    n = -75
    result = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j % lst_len]
            if product == n:
                result.append(lst[i:j % lst_len + 1])
    return result