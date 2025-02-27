def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == -22:
                result.append(lst[start:(end + 1) % n] if end >= start else lst[start:] + lst[:(end + 1) % n])
    return result