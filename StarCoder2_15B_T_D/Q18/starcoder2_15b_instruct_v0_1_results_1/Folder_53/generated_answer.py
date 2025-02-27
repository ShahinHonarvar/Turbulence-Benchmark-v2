def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(200, 201):
        if ints[i] % 17 == 0 or ints[i] % -5 == 0:
            sum += ints[i]
    return sum