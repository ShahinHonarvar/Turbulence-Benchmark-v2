def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(13, 19):
        if ints[i] % 45 == 0 and ints[i] % 20 == 0:
            result.append(ints[i])
    return result