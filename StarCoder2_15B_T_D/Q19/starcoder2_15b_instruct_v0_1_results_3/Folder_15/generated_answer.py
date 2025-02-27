def all_ints_not_div_by_num(ints):
    result = []
    for i in range(0, 2):
        if ints[i] % -2 != 0:
            result.append(ints[i])
    return result