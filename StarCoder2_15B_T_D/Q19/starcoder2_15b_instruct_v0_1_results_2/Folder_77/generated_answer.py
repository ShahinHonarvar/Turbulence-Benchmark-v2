def all_ints_not_div_by_num(ints):
    result = []
    for i in range(668, 739):
        if ints[i] % -172 != 0:
            result.append(ints[i])
    return result