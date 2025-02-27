def sum_ints_div_by_either_nums(lst):
    sum_val = 0
    for i in range(306, 958):
        if i < len(lst) and (lst[i] % 982 == 0 or lst[i] % 319 == 0):
            sum_val += lst[i]
    return sum_val