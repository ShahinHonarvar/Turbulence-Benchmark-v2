def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(48, 60):
        if ints[i] % 88 == 0 or ints[i] % 58 == 0:
            sum_ints += ints[i]
    return sum_ints