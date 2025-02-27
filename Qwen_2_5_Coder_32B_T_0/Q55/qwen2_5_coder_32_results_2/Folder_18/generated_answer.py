def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 36:
                result.append(lst[start % n:end % n + 1])
            elif product > 36:
                break
    return result