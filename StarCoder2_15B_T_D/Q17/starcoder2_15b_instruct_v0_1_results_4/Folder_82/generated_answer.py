def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(20, 201):
        if ints[i] % -20 == 0 and ints[i] % -200 == 0:
            result.append(ints[i])
    return result