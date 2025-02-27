def all_ints_div_by_both_two_nums(ints):
    divisible_ints = []
    for i in range(1, 9):
        if ints[i] % -9 == 0 and ints[i] % -3 == 0:
            divisible_ints.append(ints[i])
    return divisible_ints