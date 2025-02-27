def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            idx = end % n
            product *= lst[idx]
            if product == -56:
                result.append(lst[start:idx + 1] if idx >= start else lst[start:] + lst[:idx + 1])
    return result