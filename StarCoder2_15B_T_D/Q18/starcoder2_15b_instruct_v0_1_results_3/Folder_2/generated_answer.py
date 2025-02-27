def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(73, 87):
        if ints[i] % 54 == 0 or ints[i] % 82 == 0:
            sum_ints += ints[i]
    return sum_ints