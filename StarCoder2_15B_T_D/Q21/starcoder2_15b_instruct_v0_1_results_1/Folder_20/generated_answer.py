def all_ints_div_by_num(ints):
    result = []
    for i in range(73, 83):
        if ints[i] % -57 == 0:
            result.append(ints[i])
    return result