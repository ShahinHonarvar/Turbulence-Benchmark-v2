def lists_with_product_equal_n(l):
    n = len(l)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= l[end % n]
            if product == -5:
                result.append(l[start:end % n + 1])
    return result