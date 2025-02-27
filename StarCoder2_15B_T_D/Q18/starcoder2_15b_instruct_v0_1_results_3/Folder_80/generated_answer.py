def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(14, 94):
        if ints[i] % 71 == 0 or ints[i] % 81 == 0:
            sum += ints[i]
    return sum