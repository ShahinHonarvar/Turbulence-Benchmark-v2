def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j]
            if len(sublist) == 0:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == -3:
                results.append(sublist)
    return results