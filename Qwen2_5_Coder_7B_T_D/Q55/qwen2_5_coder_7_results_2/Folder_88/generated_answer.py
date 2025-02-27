def lists_with_product_equal_n(lst):
    n = -56
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, size + start):
            product *= lst[end % size]
            if product == n:
                result.append(lst[start:end % size])
            elif product > n:
                break
    return result