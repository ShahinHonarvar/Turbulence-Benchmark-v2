def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(51, 77):
        if ints[i] % 90 == 0 or ints[i] % 59 == 0:
            sum += ints[i]
    return sum