def lists_with_product_equal_n(lst):
    n = 537
    result = []
    lst_len = len(lst)
    for start in range(lst_len):
        product = 1
        for end in range(start, start + lst_len):
            product *= lst[end % lst_len]
            if product == n:
                result.append(lst[start % lst_len:end % lst_len + 1])
            elif product > n:
                break
    return result