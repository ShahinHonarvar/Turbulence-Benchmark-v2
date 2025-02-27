def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[10:77], start=10) if i >= 10 and (x % -40 == 0 or x % -12 == 0)))