def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(13, 77):
        if i < len(lst) and (lst[i] % -66 == 0 or lst[i] % -32 == 0):
            s += lst[i]
    return s