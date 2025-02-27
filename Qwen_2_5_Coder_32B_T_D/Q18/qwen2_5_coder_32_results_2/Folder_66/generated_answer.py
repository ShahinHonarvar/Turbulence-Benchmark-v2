def sum_ints_div_by_either_nums(lst):
    if len(lst) < 82:
        return 0
    return sum((x for x in lst[58:82] if x % 55 == 0 or x % 10 == 0))