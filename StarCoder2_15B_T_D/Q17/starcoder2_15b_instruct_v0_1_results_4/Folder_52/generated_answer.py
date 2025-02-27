def all_ints_div_by_both_two_nums(ints_list):
    result = []
    for i in range(48, 60):
        if ints_list[i] % 88 == 0 and ints_list[i] % 58 == 0:
            result.append(ints_list[i])
    return result