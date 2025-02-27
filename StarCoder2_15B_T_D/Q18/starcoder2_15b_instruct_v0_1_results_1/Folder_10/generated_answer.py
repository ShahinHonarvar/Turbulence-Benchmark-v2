def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(32, 100):
        if ints[i] % -11 == 0 or ints[i] % -15 == 0:
            sum += ints[i]
    return sum