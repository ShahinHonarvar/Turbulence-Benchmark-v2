def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + i):
            product = 1
            for k in range(i, j):
                product *= circular_list[k % n]
            if product == -17:
                sublists.append(circular_list[i:j])
    return sublists