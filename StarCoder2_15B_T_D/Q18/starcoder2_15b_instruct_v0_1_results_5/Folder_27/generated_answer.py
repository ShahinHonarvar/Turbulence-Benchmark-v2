def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(20, 36):
        if ints[i] % 36 == 0 or ints[i] % 89 == 0:
            sum += ints[i]
    return sum