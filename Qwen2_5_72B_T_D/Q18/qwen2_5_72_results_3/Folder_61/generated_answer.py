def sum_ints_div_by_either_nums(lst):
    if len(lst) < 7:
        return 0
    total = 0
    for i in range(7):
        if lst[i] % -5 == 0 or lst[i] % -6 == 0:
            total += lst[i]
    return total