def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(28, 97):
        quotient, remainder = divmod(ints[i], 90)
        if remainder == 0:
            sum_ints += ints[i]
            continue
        quotient, remainder = divmod(ints[i], 97)
        if remainder == 0:
            sum_ints += ints[i]
    return sum_ints