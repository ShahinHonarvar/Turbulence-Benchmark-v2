def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(48, 59 + 1):
        if ints[i] % 88 == 0 and ints[i] % 58 == 0:
            result.append(ints[i])
    return result