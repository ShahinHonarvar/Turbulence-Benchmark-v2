def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(93, 95):
        if ints[i] % -53 == 0 or ints[i] % -91 == 0:
            sum_ints += ints[i]
    return sum_ints