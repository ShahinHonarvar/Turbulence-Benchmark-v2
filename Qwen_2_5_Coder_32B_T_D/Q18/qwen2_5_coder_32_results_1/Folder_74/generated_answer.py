def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(90, 98):
        if i < len(lst) and (lst[i] % 13 == 0 or lst[i] % 35 == 0):
            s += lst[i]
    return s