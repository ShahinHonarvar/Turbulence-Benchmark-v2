def lists_with_product_equal_n(lst):
    n = 90
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= lst[end % size]
            if product == n:
                result.append(lst[start:end + 1] if end < start + size else lst[start:] + lst[:end % size + 1])
            if product == 0 or product > n:
                break
    return result