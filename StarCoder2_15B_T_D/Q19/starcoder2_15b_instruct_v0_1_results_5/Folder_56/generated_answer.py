def all_ints_not_div_by_num(ints):
    output = []
    for i in range(len(ints)):
        if i >= 7 and i < 9 and (ints[i] % -9 != 0):
            output.append(ints[i])
    return output