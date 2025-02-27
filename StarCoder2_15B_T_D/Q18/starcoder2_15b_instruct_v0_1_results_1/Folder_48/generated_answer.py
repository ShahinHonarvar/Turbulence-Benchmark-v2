def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(306, 958):
        if ints[i] % 982 == 0 or ints[i] % 319 == 0:
            sum += ints[i]
    return sum