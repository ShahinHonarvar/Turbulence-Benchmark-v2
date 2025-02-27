def lists_with_product_equal_n(lst):
    target_product = 76
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == target_product:
                result.append(lst[start:end % n + 1])
            elif product > target_product:
                break
    return result