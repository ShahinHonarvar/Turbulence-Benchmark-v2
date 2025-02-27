def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(56, 89):
        if ints[i] % -59 == 0 or ints[i] % -79 == 0:
            total += ints[i]
    return total