def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(58, 76):
        if ints[i] % 72 == 0 and ints[i] % 62 == 0:
            result.append(ints[i])
    return result