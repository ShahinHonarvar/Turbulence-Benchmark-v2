def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(0, 6):
        if ints[i] % -1 == 0 or ints[i] % 13 == 0:
            sum += ints[i]
    return sum