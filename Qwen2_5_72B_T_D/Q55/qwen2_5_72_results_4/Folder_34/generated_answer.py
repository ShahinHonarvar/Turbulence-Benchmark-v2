def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= lst[idx]
            if product == -81:
                result.append(lst[start:idx + 1])
            elif abs(product) > 81:
                break
    return result