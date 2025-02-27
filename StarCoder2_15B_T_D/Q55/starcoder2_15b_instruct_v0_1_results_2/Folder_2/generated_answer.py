def lists_with_product_equal_n(circular_list):
    n = -968
    sublists = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            sublist = circular_list[i:j]
            if len(sublist) > size:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists