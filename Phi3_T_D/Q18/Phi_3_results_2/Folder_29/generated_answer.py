def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(55, 85):
        if int_list[i] % -24 == 0 or int_list[i] % -11 == 0:
            result += int_list[i]
    return result