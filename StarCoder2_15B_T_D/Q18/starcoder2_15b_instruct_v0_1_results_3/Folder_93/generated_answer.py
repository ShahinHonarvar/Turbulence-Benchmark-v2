def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(86, 90):
        if int_list[i] % -61 == 0 or int_list[i] % -79 == 0:
            total += int_list[i]
    return total