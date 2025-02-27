def all_ints_div_by_both_two_nums(ints):
    divisible_ints = []
    for i in range(len(ints)):
        if i >= 58 and i <= 75 and (ints[i] % 72 == 0) and (ints[i] % 62 == 0):
            divisible_ints.append(ints[i])
    return divisible_ints