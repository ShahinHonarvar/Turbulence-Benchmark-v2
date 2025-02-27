def all_ints_div_by_num(ints):
    result = []
    for i in range(8, 8 + 1):
        if ints[i] % -7 == 0:
            result.append(ints[i])
    return result