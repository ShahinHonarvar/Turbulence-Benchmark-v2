def sum_ints_div_by_either_nums(ints_list):
    ints_div_by_either = []
    for i in range(len(ints_list)):
        if i >= 46 and i <= 91 and (ints_list[i] % 67 == 0 or ints_list[i] % 15 == 0):
            ints_div_by_either.append(ints_list[i])
    return sum(ints_div_by_either)