def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(10, 77):
        if ints[i] % -40 == 0 and ints[i] % -12 == 0:
            result.append(ints[i])
    return result