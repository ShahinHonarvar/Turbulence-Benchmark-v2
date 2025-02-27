def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(40, 201):
        if ints[i] % 21 == 0 and ints[i] % 71 == 0:
            result.append(ints[i])
    return result