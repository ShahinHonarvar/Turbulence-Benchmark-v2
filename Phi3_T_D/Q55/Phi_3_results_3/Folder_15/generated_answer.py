def lists_with_product_equal_n(circ_list):
    N = -7
    result = []
    for i in range(len(circ_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circ_list)):
            sublist.append(circ_list[j % len(circ_list)])
            product *= circ_list[j % len(circ_list)]
            if product == N and len(sublist) > 1:
                result.append(sublist.copy())
            if product == 0:
                break
    return result