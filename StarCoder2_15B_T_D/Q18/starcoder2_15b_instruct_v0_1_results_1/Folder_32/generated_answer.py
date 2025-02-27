def sum_ints_div_by_either_nums(ints_list):
    sum_ints = 0
    for i in range(len(ints_list)):
        if i >= 25 and i <= 95:
            if ints_list[i] % 51 == 0 or ints_list[i] % 77 == 0:
                sum_ints += ints_list[i]
    return sum_ints