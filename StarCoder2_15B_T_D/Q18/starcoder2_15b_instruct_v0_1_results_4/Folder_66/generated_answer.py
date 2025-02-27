def sum_ints_div_by_either_nums(ints):
    sum_of_ints = 0
    for i in range(58, 82):
        if ints[i] % 55 == 0 or ints[i] % 10 == 0:
            sum_of_ints += ints[i]
    return sum_of_ints