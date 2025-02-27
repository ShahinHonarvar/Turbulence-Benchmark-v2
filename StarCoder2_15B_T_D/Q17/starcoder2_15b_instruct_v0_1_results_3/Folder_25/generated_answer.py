def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(25, 81):
        if ints[i] % -20 == 0 and ints[i] % -26 == 0:
            result.append(ints[i])
    return result