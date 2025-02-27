def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(281, 695):
        if ints[i] % -722 == 0 or ints[i] % -731 == 0:
            sum += ints[i]
    return sum