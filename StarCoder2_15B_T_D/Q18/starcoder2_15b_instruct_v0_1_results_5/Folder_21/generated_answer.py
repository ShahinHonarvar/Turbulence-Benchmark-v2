def sum_ints_div_by_either_nums(ints):
    sum_divisible = 0
    for i in range(315, 935):
        if ints[i] % -897 == 0 or ints[i] % -556 == 0:
            sum_divisible += ints[i]
    return sum_divisible