def all_ints_div_by_both_two_nums(ints_list):
    result = []
    for i in range(10, 80):
        if ints_list[i] % -74 == 0 and ints_list[i] % -58 == 0:
            result.append(ints_list[i])
    return result