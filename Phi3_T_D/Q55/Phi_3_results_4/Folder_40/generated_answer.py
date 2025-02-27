def lists_with_product_equal_n(cyclic_list):
    length = len(cyclic_list)
    sublists = []
    for i in range(length):
        curr_product = 1
        sub = []
        for j in range(length):
            index = (i + j) % length
            curr_product *= cyclic_list[index]
            if curr_product == -9:
                sub.append(cyclic_list[index])
                sublists.append(sub.copy())
                curr_product = 1
            elif curr_product < 0 or curr_product > -9:
                break
    return sublists