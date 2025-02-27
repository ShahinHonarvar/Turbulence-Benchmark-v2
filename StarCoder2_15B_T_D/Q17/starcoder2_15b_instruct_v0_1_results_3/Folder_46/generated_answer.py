def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(11, 47):
        if ints[i] % 55 == 0 and ints[i] % 36 == 0:
            result.append(ints[i])
    return result