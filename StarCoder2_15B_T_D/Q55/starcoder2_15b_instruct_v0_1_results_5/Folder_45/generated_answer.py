def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        temp = []
        product = 1
        for j in range(i, i + n):
            index = j % n
            product *= lst[index]
            temp.append(lst[index])
            if product == -5:
                result.append(temp[:])
        if product == -5:
            result.append(temp[:])
    return result