def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(86, 90):
        if ints[i] % -61 == 0 or ints[i] % -79 == 0:
            sum += ints[i]
    return sum