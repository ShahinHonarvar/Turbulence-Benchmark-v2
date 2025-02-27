def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(57, 86):
        if i < len(lst) and (lst[i] % -77 == 0 or lst[i] % -32 == 0):
            s += lst[i]
    return s