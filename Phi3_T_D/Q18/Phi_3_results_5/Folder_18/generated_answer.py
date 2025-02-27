def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(55, 67):
        if int_list[i] % 22 == 0 or int_list[i] % 82 == 0:
            total_sum += int_list[i]
    return total_sum