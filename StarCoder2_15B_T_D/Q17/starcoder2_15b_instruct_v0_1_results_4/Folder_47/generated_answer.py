def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(42, 88):
        if ints[i] % -90 == 0 and ints[i] % -74 == 0:
            result.append(ints[i])
    return result