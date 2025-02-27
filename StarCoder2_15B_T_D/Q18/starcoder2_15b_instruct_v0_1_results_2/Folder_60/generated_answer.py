def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(10, 80):
        if ints[i] % -74 == 0 or ints[i] % -58 == 0:
            sum += ints[i]
    return sum