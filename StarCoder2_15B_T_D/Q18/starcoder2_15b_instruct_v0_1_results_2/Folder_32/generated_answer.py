def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(25, 96):
        if ints[i] % 51 == 0 or ints[i] % 77 == 0:
            sum += ints[i]
    return sum