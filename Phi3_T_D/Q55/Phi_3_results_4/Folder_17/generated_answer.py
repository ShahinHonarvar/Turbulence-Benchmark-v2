def lists_with_product_equal_n(circular_list):
    target = 18
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n + i):
            sliced = circular_list[i:j % n]
            product_sum = 1
            for num in sliced:
                product_sum *= num
            if product_sum == target:
                sublists.append(sliced)
    return sublists