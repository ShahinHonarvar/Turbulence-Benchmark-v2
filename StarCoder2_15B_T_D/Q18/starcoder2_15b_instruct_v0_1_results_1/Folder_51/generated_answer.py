def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(6, 10):
        if ints[i] % -1 == 0 or ints[i] % -10 == 0:
            total += ints[i]
    return total