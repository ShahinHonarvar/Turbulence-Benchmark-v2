def lists_with_product_equal_n(lst):
    n = 49
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    for i in range(size):
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == n:
                result.append(lst[j:i + 1])
            elif product > n:
                break
    return result