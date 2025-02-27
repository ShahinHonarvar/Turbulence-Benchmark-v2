def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    target_product = -95
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == target_product:
                results.append(lst[start:end % n + 1])
            elif abs(product) > abs(target_product):
                break
    return results