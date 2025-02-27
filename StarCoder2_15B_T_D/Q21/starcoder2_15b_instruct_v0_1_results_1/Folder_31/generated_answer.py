def all_ints_div_by_num(ints):
    result = []
    if len(ints) < 20:
        return result
    for i in range(66, 75):
        if ints[i] % -14 == 0:
            result.append(ints[i])
    return result