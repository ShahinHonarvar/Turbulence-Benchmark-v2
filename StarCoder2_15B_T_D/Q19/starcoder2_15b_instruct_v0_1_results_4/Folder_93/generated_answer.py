def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(33, 78):
        if int_list[i] % -17 != 0:
            result.append(int_list[i])
    return result