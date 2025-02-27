def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(543, 585):
        if ints[i] % -553 == 0 or ints[i] % -737 == 0:
            sum += ints[i]
    return sum