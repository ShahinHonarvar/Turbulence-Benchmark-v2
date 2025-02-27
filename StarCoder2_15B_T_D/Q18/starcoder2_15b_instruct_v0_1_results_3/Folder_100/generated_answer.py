def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(72, 94):
        if ints[i] % 32 == 0 or ints[i] % 44 == 0:
            sum_ints += ints[i]
    return sum_ints