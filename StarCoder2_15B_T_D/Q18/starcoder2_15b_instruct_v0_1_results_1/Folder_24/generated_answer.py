def sum_ints_div_by_either_nums(ints_list):
    if not ints_list or len(ints_list) < 54:
        return 0
    sum = 0
    for i in range(29, 54):
        if ints_list[i] % -68 == 0 or ints_list[i] % -85 == 0:
            sum += ints_list[i]
    return sum