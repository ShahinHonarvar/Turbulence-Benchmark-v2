def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 990:
                result.append(lst[start % n:end % n + 1] if end >= start else lst[start % n:] + lst[:end % n + 1])
            if product == 0:
                break
    return result