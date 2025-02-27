def all_ints_not_div_by_num(int_list):
    output_list = []
    for i in range(48, 62):
        if i % 28 != 0:
            output_list.append(int_list[i])
    return output_list