def sum_ints_div_by_either_nums(ints):
    sum_of_ints = 0
    for i in range(69, 98):
        if ints[i] % -90 == 0 or ints[i] % -67 == 0:
            sum_of_ints += ints[i]
    return sum_of_ints