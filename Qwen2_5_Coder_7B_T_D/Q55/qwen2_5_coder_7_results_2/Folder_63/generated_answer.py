def lists_with_product_equal_n(lst):
    result = []
    n = 96
    size = len(lst)
    for start in range(size):
        product = 1
        for length in range(1, size - start + 1):
            product *= lst[(start + length - 1) % size]
            if product == n:
                result.append(lst[start:start + length])
            elif product > n:
                break
    return result