def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for i in range(13, 92):
        if int_list[i] % -65 == 0 or int_list[i] % -62 == 0:
            sum_ints += int_list[i]
    return sum_ints