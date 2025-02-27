def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 851:
                result.append(lst[start % n:end % n + 1])
            elif product > 851:
                break
    return result