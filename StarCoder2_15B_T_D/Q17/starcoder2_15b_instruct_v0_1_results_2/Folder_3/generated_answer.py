def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(38, 53):
        if ints[i] % -41 == 0 and ints[i] % -47 == 0:
            result.append(ints[i])
    return result