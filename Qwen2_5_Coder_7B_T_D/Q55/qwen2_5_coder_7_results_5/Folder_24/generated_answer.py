def lists_with_product_equal_n(lst):
    n = -89
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length) % size
            product *= lst[end]
            if product == n:
                result.append(lst[start:end])
            elif product > abs(n):
                break
    return result