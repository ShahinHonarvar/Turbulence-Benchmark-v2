def lists_with_product_equal_n(lst, n=13):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, i + size):
            sublist_prod = 1
            for k in range(i, j):
                sublist_prod *= lst[k % size]
            if sublist_prod == n:
                result.append([lst[k % size] for k in range(i, j)])
    return result