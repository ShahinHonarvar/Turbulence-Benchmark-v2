def lists_with_product_equal_n(lst):
    n = 32
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= lst[end % length]
            if product == n:
                result.append(lst[start:end % length + 1] if end % length >= start else lst[start:] + lst[:end % length + 1])
            if product > n:
                break
    return result