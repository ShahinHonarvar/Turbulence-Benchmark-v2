def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(77, 88):
        if ints[i] % 23 == 0 and ints[i] % 57 == 0:
            result.append(ints[i])
    return result