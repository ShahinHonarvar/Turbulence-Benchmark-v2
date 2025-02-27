def all_ints_not_div_by_num(ints):
    result = []
    for i in range(len(ints)):
        if i >= 43 and i < 77 and (ints[i] % 84 != 0):
            result.append(ints[i])
    return result