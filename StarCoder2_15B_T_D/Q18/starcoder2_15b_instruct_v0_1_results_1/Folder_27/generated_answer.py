def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for i in range(20, 36):
        if int_list[i] % -36 == 0 or int_list[i] % -89 == 0:
            sum_ints += int_list[i]
    return sum_ints