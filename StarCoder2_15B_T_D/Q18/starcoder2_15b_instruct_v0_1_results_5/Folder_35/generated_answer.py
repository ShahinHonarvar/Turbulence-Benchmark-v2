def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(77, 88):
        if ints[i] % 23 == 0 or ints[i] % 57 == 0:
            sum_ints += ints[i]
    return sum_ints