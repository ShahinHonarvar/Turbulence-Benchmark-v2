def lists_with_product_equal_n(circular_list):
    n = -91
    result = []
    for i in range(len(circular_list)):
        curr_list = []
        curr_prod = 1
        for j in range(i, i + len(circular_list)):
            curr_list.append(circular_list[j % len(circular_list)])
            curr_prod *= circular_list[j % len(circular_list)]
            if curr_prod == n:
                result.append(curr_list)
            elif curr_prod == 0:
                break
    return result