def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(len(ints)):
        if i >= 0 and i <= 2 and (ints[i] % -2 == 0) and (ints[i] % 3 == 0):
            result.append(ints[i])
    return result