def all_ints_div_by_num(ints):
    result = []
    for i in range(62, 71):
        if ints[i] % 58 == 0:
            result.append(ints[i])
    return result