def sum_ints_div_by_either_nums(lst):
    if len(lst) < 46:
        return 0
    return sum((x for i, x in enumerate(lst[29:46]) if x % 27 == 0 or x % 81 == 0))