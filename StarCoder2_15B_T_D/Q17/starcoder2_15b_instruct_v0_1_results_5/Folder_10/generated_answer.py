def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(32, 100):
        if ints[i] % -11 == 0 and ints[i] % -15 == 0:
            result.append(ints[i])
    return result