def lists_with_product_equal_n(lst):
    n = 27
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            idx = j % size
            product *= lst[idx]
            if product == n:
                result.append(lst[i:idx + 1] if i <= idx else lst[i:] + lst[:idx + 1])
            elif product > n:
                break
    return result