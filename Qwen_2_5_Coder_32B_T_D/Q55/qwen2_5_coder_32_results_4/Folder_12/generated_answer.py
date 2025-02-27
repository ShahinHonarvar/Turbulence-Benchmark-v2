def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n - 1):
            product *= lst[end % n]
            if product == -18:
                result.append(lst[start % n:(end + 1) % n] if (end + 1) % n >= start % n else lst[start % n:] + lst[:(end + 1) % n])
    return result