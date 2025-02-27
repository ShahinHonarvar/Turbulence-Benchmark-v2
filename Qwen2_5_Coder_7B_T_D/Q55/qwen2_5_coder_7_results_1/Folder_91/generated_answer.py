def lists_with_product_equal_n(lst):
    n = 2
    result = []
    lst = lst * 2
    for i in range(len(lst) // 2):
        product = 1
        for j in range(i, i + len(lst) // 2):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j])
            elif product > n:
                break
    return result