def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= lst[(start + end) % n]
            if product == 36:
                result.append(lst[start:(start + end + 1) % n] if start + end + 1 > n else lst[start:start + end + 1])
            elif product > 36:
                break
    return result