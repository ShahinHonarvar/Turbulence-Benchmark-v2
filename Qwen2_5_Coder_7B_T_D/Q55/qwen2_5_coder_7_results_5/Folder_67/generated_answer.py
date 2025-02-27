def lists_with_product_equal_n(lst):
    n = 33
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        temp = []
        for j in range(i, size + i):
            product *= lst[j % size]
            temp.append(lst[j % size])
            if product == n:
                result.append(temp)
            elif product > n:
                break
    return result