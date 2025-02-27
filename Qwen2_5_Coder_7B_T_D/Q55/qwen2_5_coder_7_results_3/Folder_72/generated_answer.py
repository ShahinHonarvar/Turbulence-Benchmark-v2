def lists_with_product_equal_n(lst):
    n = 10
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j % size]
            if product == n:
                result.append(lst[i:j % size + 1])
            elif product > n:
                break
    return result