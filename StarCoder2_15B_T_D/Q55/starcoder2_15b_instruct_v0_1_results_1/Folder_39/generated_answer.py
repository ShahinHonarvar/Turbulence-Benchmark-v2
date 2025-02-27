def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            if len(sublist) <= n and abs(1 + sum(sublist)) == 46:
                sublists.append(sublist)
    return sublists