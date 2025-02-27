def sum_ints_div_by_either_nums(ints_list):
    sum_ints = 0
    for i in range(len(ints_list)):
        if i >= 90 and i <= 200 and (ints_list[i] % -31 == 0 or ints_list[i] % 13 == 0):
            sum_ints += ints_list[i]
    return sum_ints