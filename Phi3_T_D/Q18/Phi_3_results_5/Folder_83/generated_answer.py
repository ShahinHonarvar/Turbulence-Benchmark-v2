def sum_ints_div_by_either_nums(int_list):
    sum_res = 0
    for i in range(90, 201):
        if int_list[i] % -31 == 0 or int_list[i] % 13 == 0:
            sum_res += int_list[i]
    return sum_res