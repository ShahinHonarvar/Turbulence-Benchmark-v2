def lists_with_product_equal_n(lst):
    n = 13
    result = []
    len_lst = len(lst)
    for start in range(len_lst):
        product = 1
        for end in range(start, start + len_lst):
            product *= lst[end % len_lst]
            if product == n:
                result.append(lst[start:end + 1])
    return result