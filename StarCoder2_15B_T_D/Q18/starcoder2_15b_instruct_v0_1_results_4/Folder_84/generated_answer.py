def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(78, 82):
        if ints[i] % 76 == 0 or ints[i] % 60 == 0:
            sum += ints[i]
    return sum