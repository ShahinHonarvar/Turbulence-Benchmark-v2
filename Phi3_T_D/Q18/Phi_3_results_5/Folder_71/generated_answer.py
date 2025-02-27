def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(68, 100):
        if int_list[i] % -37 == 0 or int_list[i] % -26 == 0:
            total += int_list[i]
    return total