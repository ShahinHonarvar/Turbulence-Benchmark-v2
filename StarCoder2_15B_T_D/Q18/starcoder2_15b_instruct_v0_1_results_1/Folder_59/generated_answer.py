def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(len(ints)):
        if i >= 0 and i <= 8:
            if ints[i] % -3 == 0 or ints[i] % 8 == 0:
                sum_ints += ints[i]
    return sum_ints