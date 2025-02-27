def lists_with_product_equal_n(circular_list):
    product = 714
    n = len(circular_list)
    sublists = []
    for i in range(n):
        temp_product = 1
        for j in range(i, n + i):
            temp_product *= circular_list[j % n]
            if temp_product == product:
                sublists.append(circular_list[i:j + 1])
    return sublists