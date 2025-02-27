def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(240, 902):
        if ints[i] % 546 == 0 and ints[i] % 709 == 0:
            result.append(ints[i])
    return result