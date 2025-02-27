def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i < j and i != j - 1 and (lst[i] * lst[j - 1] == 2):
                result.append(lst[i:j])
    return result