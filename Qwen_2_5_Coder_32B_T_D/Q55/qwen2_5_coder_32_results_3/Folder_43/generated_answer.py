def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            product *= lst[(start + size - 1) % n]
            if product == -26:
                result.append(lst[start:start + size] + lst[:size - (n - start)])
    return result