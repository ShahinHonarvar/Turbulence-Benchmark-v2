def lists_with_product_equal_n(circular_list):
    n = -89
    len_list = len(circular_list)
    res = []
    for i in range(len_list):
        cur_product = 1
        for j in range(i, i + len_list):
            cur_product *= circular_list[j % len_list]
            if cur_product == n:
                res.append(circular_list[i:j + 1])
            elif cur_product > n:
                break
    return res