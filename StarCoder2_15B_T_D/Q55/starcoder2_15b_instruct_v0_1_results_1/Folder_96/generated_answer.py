def lists_with_product_equal_n(circ_list):
    n = len(circ_list)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circ_list[i:j]
            if len(sublist) <= n and 0 in sublist and (len(sublist) > 1):
                sublists.append(sublist)
    return sublists