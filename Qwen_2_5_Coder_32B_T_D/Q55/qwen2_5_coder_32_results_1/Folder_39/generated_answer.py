def lists_with_product_equal_n(lst):
    n = -46
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            index = j % size
            product *= lst[index]
            if product == n:
                result.append(lst[i:index + 1])
    return result