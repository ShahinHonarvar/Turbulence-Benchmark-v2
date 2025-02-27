def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -54:
                sublists.append(sublist)
    return sublists