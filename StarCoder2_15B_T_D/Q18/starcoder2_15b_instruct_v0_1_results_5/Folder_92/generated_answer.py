def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(len(ints)):
        if ints[i] % 1 == 0 or ints[i] % -1 == 0:
            total += ints[i]
    return total