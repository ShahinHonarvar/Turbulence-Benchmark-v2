def sum_ints_div_by_either_nums(ints_list):
    sum_ints = 0
    for i in range(54, 80):
        if ints_list[i] % 54 == 0 or ints_list[i] % 28 == 0:
            sum_ints += ints_list[i]
    return sum_ints