def all_ints_not_div_by_num(ints):
    result = []
    for i in range(59, 93):
        if ints[i] % -26 != 0:
            result.append(ints[i])
    return result