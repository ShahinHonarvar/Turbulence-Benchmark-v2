def lists_with_product_equal_n(lst):
    n = 76
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for i in range(size):
            product *= lst[(start + i) % size]
            if product == n:
                result.append(lst[start:start + i + 1])
            elif product > n:
                break
    return result