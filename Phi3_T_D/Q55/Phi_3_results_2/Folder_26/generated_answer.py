def lists_with_product_equal_n(cyclic_list):
    result = []
    n = len(cyclic_list)
    for i in range(n):
        for j in range(i, n + i):
            if i != j:
                sub_list = cyclic_list[i % n:j % n]
                if len(sub_list) > 0 and (i < n and j < n) or (seq := sub_list) == [1] * len(seq):
                    product = 1
                    for num in sub_list:
                        product *= num
                    if product == 93:
                        result.append(sub_list)
    return result