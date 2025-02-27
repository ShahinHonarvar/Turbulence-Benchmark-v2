def all_ints_div_by_num(ints):
    result = []
    for i in range(42, 98):
        if ints[i] % 46 == 0:
            result.append(ints[i])
    return result