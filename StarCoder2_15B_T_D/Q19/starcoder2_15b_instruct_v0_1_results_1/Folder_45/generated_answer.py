def all_ints_not_div_by_num(ints):
    result = []
    for i in range(30, 200):
        if ints[i] % -115 != 0:
            result.append(ints[i])
    return result