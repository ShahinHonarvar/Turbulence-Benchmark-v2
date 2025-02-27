def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(len(ints)):
        if ints[i] % -74 == 0 or ints[i] % -58 == 0:
            if 10 <= i <= 79:
                sum_ints += ints[i]
    return sum_ints