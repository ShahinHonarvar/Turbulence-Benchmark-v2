def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 57:
                result.append(lst[start:end % n + 1] if start <= end % n else lst[start:] + lst[:end % n + 1])
            elif product == 0:
                break
    return result