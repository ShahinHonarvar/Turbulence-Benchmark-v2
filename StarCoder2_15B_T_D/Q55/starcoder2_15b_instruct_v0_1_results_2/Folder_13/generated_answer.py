def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i < j - 1 and lst[i] * lst[i + 1] == 54:
                sublists.append(lst[i:j])
            elif i == j - 1 and lst[-1] * lst[0] == 54:
                sublists.append(lst[i:] + lst[:j])
    return sublists