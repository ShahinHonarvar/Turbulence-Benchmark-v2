def lists_with_product_equal_n(lst):
    n = 851
    result = []
    l = len(lst)
    for i in range(l):
        product = 1
        for j in range(i, i + l):
            index = j % l
            product *= lst[index]
            if product == n:
                result.append(lst[i:index + 1])
            elif product > n:
                break
    return result