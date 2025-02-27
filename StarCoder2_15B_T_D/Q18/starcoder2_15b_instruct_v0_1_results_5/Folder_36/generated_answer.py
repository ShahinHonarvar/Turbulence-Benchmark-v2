def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(299, 383):
        if ints[i] % 858 == 0 or ints[i] % 952 == 0:
            sum += ints[i]
    return sum