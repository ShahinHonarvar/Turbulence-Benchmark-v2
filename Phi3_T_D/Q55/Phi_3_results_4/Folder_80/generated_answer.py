def lists_with_product_equal_n(cyclic_list):
    result = []
    length = len(cyclic_list)
    for i in range(length):
        for j in range(i + 1, length + i):
            product = 1
            sublist = []
            for k in range(i, j % length):
                product *= cyclic_list[k % length]
                sublist.append(cyclic_list[k % length])
            if product == 43:
                result.append(sublist)
    return result