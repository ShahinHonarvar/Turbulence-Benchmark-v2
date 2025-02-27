def lists_with_product_equal_n(circ_list):
    n = len(circ_list)
    result = []
    if n < 2:
        return result
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            if product == -1:
                if len(sublist) > 1:
                    result.append(sublist)
                product = 0
                sublist = []
                break
            else:
                product *= circ_list[(i + j) % n]
                sublist.append(circ_list[(i + j) % n])
        if sublist and product == -1:
            result.append(sublist)
    return result