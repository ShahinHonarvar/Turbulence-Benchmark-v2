def all_ints_not_div_by_num(integers):
    result = []
    for i in range(len(integers)):
        if i >= 93 and i < 94 and (integers[i] % 57 != 0):
            result.append(integers[i])
    return result