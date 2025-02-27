def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for i in range(93, 95):
        if int_list[i] % -53 == 0 or int_list[i] % -91 == 0:
            sum_ints += int_list[i]
    return sum_ints