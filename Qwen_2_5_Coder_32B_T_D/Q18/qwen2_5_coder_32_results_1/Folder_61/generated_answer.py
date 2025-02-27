def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(min(7, len(lst))):
        if lst[i] % -5 == 0 or lst[i] % -6 == 0:
            s += lst[i]
    return s