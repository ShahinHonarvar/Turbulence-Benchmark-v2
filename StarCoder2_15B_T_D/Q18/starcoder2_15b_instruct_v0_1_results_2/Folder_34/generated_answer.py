def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for i in range(60, 201):
        if int_list[i] % 9 == 0 or int_list[i] % 11 == 0:
            sum_of_ints += int_list[i]
    return sum_of_ints