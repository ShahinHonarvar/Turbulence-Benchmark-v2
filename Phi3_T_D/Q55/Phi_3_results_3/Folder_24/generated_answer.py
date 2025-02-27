def lists_with_product_equal_n(circular_list):
    n = -89
    if circular_list[0] == 0 and n == 0:
        return [circular_list[:1]]
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            i %= len(circular_list)
            sublist_product = 1
            sublist = []
            for k in range(i, j % len(circular_list)):
                sublist_product *= circular_list[k]
                sublist.append(circular_list[k])
                if sublist_product == n:
                    result.append(sublist)
    return result