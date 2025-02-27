def lists_with_product_equal_n(lst):
    n = 8
    result = []
    N = len(lst)
    for i in range(N):
        product = 1
        for j in range(i, N + i):
            product *= lst[j % N]
            if product == n:
                result.append(lst[i:j % N + 1])
            elif product > n:
                break
    return result