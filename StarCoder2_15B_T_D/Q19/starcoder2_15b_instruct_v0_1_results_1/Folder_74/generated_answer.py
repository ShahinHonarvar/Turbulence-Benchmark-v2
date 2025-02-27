def all_ints_not_div_by_num(ints):
    result = []
    for i in range(len(ints)):
        if i >= 93 and i < 94 and (ints[i] % 57 != 0):
            result.append(ints[i])
    return result