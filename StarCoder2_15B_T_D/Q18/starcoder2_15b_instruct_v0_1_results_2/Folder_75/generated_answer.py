def sum_ints_div_by_either_nums(ints):
    sum_of_ints = 0
    for i in range(20, 94):
        if ints[i] % -92 == 0 or ints[i] % -50 == 0:
            sum_of_ints += ints[i]
    return sum_of_ints