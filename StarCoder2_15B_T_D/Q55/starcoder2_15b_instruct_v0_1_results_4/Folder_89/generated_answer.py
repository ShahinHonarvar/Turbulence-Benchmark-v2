def lists_with_product_equal_n(lst):
    n = 57
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if n % lst[i] == 0:
                sublists.append(lst[i:j])
    return sublists