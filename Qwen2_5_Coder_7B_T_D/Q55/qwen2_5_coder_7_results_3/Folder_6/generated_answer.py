def lists_with_product_equal_n(lst):
    n = 42
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i + j) % size]
            if product == n:
                result.append(lst[i:i + j + 1])
            elif product > n:
                break
    return result