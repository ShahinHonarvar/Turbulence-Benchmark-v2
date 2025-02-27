def all_ints_div_by_both_two_nums(ints):
    output = []
    for i in range(7, 10):
        if ints[i] % -9 == 0 and ints[i] % -7 == 0:
            output.append(ints[i])
    return output