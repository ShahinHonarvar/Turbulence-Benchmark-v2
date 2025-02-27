def lists_with_product_equal_n(lst):
    l = len(lst)
    result = []
    for start in range(l):
        product = 1
        for end in range(start, start + l):
            product *= lst[end % l]
            if product == -15:
                result.append(lst[start:end % l + 1])
    return result