def all_ints_div_by_both_two_nums(ints_list):
    result = []
    for i in range(7, 10):
        if ints_list[i] % 2 == 0 and ints_list[i] % 3 == 0:
            result.append(ints_list[i])
    return result