def lists_with_product_equal_n(lst):
    n = -61
    result = []
    lst_len = len(lst)
    for start in range(lst_len):
        product = 1
        for length in range(1, lst_len + 1):
            end = (start + length - 1) % lst_len
            product *= lst[end]
            if product == n:
                result.append(lst[start:end + 1])
    return result