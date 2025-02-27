def all_ints_div_by_num(ints):
    result = []
    for i in range(14, 57):
        if ints[i] % -59 == 0:
            result.append(ints[i])
    return result