def all_ints_not_div_by_num(ints):
    result = []
    for i in range(11, 56):
        if ints[i] % 90 != 0:
            result.append(ints[i])
    return result