def lists_with_product_equal_n(circular_list):
    result = []
    n_len = len(circular_list)
    product_target = 47
    for i in range(n_len):
        for j in range(i, n_len + i):
            sublist = circular_list[i:j % n_len]
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
            if sublist_product == product_target:
                result.append(sublist)
    return result