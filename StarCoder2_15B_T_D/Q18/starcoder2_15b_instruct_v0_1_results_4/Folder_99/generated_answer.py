def sum_ints_div_by_either_nums(ints_list):
    sum_of_ints = 0
    for i in range(154, 799):
        if ints_list[i] % 275 == 0 or ints_list[i] % 580 == 0:
            sum_of_ints += ints_list[i]
    return sum_of_ints