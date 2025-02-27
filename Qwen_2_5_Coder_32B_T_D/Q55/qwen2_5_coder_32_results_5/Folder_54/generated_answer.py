def lists_with_product_equal_n(lst):
    n = -17
    result = []
    l = len(lst)
    for start in range(l):
        product = 1
        for end in range(start, start + l):
            product *= lst[end % l]
            if product == n:
                result.append(lst[start % l:end % l + 1] if start <= end else lst[start % l:] + lst[:end % l + 1])
    return result