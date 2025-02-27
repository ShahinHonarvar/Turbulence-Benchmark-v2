def lists_with_product_equal_n(lst):
    n = 851
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    for i in range(length):
        product = 1
        for j in range(length - 1, i - 1, -1):
            product *= lst[j]
            if product == n:
                result.append(lst[j:i])
            elif product > n:
                break
    return result