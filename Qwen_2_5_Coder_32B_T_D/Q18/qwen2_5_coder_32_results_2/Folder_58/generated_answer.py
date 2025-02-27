def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(240, 902):
        if i < len(lst) and (lst[i] % 546 == 0 or lst[i] % 709 == 0):
            s += lst[i]
    return s