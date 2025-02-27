def lists_with_product_equal_n(lst):
    n = 51
    result = []
    lst_length = len(lst)
    for start in range(lst_length):
        product = 1
        for end in range(start, start + lst_length):
            product *= lst[end % lst_length]
            if product == n:
                result.append(lst[start:end % lst_length + 1])
            elif product > n:
                break
    return result