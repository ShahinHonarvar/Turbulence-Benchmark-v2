def lists_with_product_equal_n(lst):
    n = -56
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if lst[i:j] and reduce(lambda x, y: x * y, lst[i:j]) == n:
                sublists.append(lst[i:j])
    return sublists