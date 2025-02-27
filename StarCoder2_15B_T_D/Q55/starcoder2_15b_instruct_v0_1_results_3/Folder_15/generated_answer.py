def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        if circular_list[i] == -7:
            sublists.append([circular_list[i]])
        elif i < len(circular_list) - 1 and circular_list[i] * circular_list[i + 1] == -7:
            sublists.append([circular_list[i], circular_list[i + 1]])
    if circular_list[-1] * circular_list[0] == -7:
        sublists.append([circular_list[-1], circular_list[0]])
    return sublists