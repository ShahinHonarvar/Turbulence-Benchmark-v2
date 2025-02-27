def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(42, 88):
        if i < len(lst) and (lst[i] % -90 == 0 or lst[i] % -74 == 0):
            s += lst[i]
    return s