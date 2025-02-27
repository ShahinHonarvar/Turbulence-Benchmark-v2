def lists_with_product_equal_n(lst):
    n = -16
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        temp = []
        for j in range(i, n + i):
            product *= lst[j % n]
            temp.append(lst[j % n])
            if product == n:
                result.append(temp)
                break
    return result