def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(13, 77):
        if ints[i] % -66 == 0 and ints[i] % -32 == 0:
            result.append(ints[i])
    return result