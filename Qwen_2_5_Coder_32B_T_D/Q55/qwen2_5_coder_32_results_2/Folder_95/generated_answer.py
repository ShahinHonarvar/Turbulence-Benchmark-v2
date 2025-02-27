def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 28:
                result.append(lst[start:end % n + 1] if end % n >= start else lst[start:] + lst[:end % n + 1])
            elif product > 28:
                break
    return result