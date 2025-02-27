def all_ints_div_by_num(int_list):
    result = []
    for i in range(44, 74):
        if int_list[i] % 88 == 0:
            result.append(int_list[i])
    return result