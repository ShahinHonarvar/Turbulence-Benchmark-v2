def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []

    def extend_list(lst, i, j):
        return lst[i:j] + lst[:max(i, j)]
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            k = j % n
            product *= lst[k]
            if product == 100:
                result.append(extend_list(lst, i, k + 1))
    return result