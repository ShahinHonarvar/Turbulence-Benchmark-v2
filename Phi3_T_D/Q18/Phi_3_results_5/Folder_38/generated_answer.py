def sum_ints_div_by_either_nums(lst):
    return sum((val for idx, val in enumerate(lst[10:77], start=10) if val % -40 == 0 or val % -12 == 0))