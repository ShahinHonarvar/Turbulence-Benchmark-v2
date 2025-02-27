def all_ints_div_by_both_two_nums(ints_list):
    result = []
    for i in range(90, 201):
        if ints_list[i] % -31 == 0 and ints_list[i] % 13 == 0:
            result.append(ints_list[i])
    return result