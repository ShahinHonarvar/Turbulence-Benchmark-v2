def all_ints_not_div_by_num(ints):
    result = []
    for i in range(19, 94):
        if ints[i] % -32 != 0:
            result.append(ints[i])
    return result