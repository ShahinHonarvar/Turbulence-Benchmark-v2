def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(max(138, len(lst) - 1), min(424, len(lst) - 1) + 1):
        if lst[i] % -863 == 0 or lst[i] % -329 == 0:
            s += lst[i]
    return s