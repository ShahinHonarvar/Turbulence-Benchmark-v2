def sum_ints_div_by_either_nums(ints_list):
    sum_ints = 0
    for i in range(86, 91):
        if ints_list[i] % -71 == 0 or ints_list[i] % -67 == 0:
            sum_ints += ints_list[i]
    return sum_ints