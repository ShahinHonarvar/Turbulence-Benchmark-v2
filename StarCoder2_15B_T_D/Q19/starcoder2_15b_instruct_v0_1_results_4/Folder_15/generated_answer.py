def all_ints_not_div_by_num(ints):
    result = []
    for i in ints[0:2]:
        if i % -2 != 0:
            result.append(i)
    return result