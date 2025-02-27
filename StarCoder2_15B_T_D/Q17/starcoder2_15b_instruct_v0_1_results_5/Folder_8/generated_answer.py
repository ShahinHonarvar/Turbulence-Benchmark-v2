def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(36, 86):
        if ints[i] % -27 == 0 and ints[i] % -96 == 0:
            result.append(ints[i])
    return result