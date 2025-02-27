def all_ints_div_by_num(ints):
    result = []
    for i in range(3):
        if ints[i] % -8 == 0:
            result.append(ints[i])
    return result