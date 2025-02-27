def lists_with_product_equal_n(lst, n):
    res = []
    for i in range(len(lst)):
        curr_prod = lst[i]
        curr_list = [lst[i]]
        for j in range(i + 1, len(lst) + i):
            curr_prod *= lst[j % len(lst)]
            curr_list.append(lst[j % len(lst)])
            if curr_prod == n:
                res.append(curr_list)
            if curr_prod == 0:
                break
    return res