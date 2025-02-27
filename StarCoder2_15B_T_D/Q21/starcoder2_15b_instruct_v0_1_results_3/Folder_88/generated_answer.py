def all_ints_div_by_num(ints):
    result = []
    for i in range(len(ints)):
        if i >= 0 and i <= 2 and (ints[i] % -8 == 0):
            result.append(ints[i])
    return result