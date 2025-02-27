def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(1, 5):
        if ints[i] % 4 == 0 and ints[i] % -6 == 0:
            result.append(ints[i])
    return result