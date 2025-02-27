def lists_with_product_equal_n(lst):
    n = 48
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        current_list = []
        for j in range(i, n + i):
            product *= lst[j % n]
            current_list.append(lst[j % n])
            if product == n:
                result.append(current_list)
            elif product > n:
                break
    return result