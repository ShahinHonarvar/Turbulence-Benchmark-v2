def lists_with_product_equal_n(circ_list):
    n = -44
    result = []
    for i in range(len(circ_list)):
        product = 1
        for j in range(i, i + len(circ_list)):
            product *= circ_list[j % len(circ_list)]
            if product == n:
                result.append(circ_list[i:j + 1])
    return result