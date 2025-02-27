def lists_with_product_equal_n(lst):
    n = 37
    sublists = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= lst[j]
            if product == n:
                sublists.append(lst[i:j + 1])
            elif product > n:
                break
    return sublists