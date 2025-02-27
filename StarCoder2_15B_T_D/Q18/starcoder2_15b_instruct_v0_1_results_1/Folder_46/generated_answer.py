def sum_ints_div_by_either_nums(ints):
    if not ints or len(ints) < 47:
        return 0
    sum_divisible = 0
    for i in range(11, 47):
        if ints[i] % 55 == 0 or ints[i] % 36 == 0:
            sum_divisible += ints[i]
    return sum_divisible