def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(11, 47):
        if ints[i] % 55 == 0 or ints[i] % 36 == 0:
            sum += ints[i]
    return sum