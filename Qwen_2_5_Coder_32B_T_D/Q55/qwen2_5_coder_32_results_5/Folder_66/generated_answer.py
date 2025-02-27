def lists_with_product_equal_n(lst):
    n = 78
    result = []
    l = len(lst)
    for start in range(l):
        product = 1
        for end in range(start, start + l):
            product *= lst[end % l]
            if product == n:
                result.append(lst[start:end % l + 1])
            elif product > n:
                break
    return result