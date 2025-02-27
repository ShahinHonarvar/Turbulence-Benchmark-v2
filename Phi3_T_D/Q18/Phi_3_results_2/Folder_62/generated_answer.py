def sum_ints_div_by_either_nums(int_list):
    sum_val = 0
    for i in range(44, 60):
        if int_list[i] % 39 == 0 or int_list[i] % 15 == 0:
            sum_val += int_list[i]
    return sum_val