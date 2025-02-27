def all_ints_not_div_by_num(ints):
    result = []
    for i in range(495, 826):
        if ints[i] % -201 != 0:
            result.append(ints[i])
    return result