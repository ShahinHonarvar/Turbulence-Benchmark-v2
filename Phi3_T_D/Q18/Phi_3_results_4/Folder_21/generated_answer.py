def sum_ints_div_by_either_nums(int_list):
    sum_val = 0
    for i in range(315, 935):
        if int_list[i] % -897 == 0 or int_list[i] % -556 == 0:
            sum_val += int_list[i]
    return sum_val