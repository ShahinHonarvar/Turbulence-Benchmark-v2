def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(34, 82):
        if ints[i] % 27 == 0 or ints[i] % 57 == 0:
            sum += ints[i]
    return sum