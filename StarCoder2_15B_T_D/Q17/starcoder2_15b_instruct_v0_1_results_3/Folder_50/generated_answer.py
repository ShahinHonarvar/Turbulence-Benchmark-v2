def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(46, 92):
        if ints[i] % 67 == 0 and ints[i] % 15 == 0:
            result.append(ints[i])
    return result