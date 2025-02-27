def lists_with_product_equal_n(c_list):
    n = -83
    result = []
    for i in range(len(c_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(c_list)):
            index = j % len(c_list)
            product *= c_list[index]
            sublist.append(c_list[index])
            if product == n:
                result.append(sublist)
                break
            elif product > abs(n):
                break
    return result