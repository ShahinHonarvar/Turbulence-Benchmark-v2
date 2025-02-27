def lists_with_product_equal_n(lst):
    n = -10
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if lst[i:j] and n % abs(reduce(lambda x, y: x * y, lst[i:j])) == 0:
                sublists.append(lst[i:j])
    return sublists