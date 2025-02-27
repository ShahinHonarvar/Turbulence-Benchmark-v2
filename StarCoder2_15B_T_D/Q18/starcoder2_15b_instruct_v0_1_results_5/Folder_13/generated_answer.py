def sum_ints_div_by_either_nums(ints):
    sum_of_ints = 0
    for i in range(13, 19):
        if ints[i] % 45 == 0 or ints[i] % 20 == 0:
            sum_of_ints += ints[i]
    return sum_of_ints