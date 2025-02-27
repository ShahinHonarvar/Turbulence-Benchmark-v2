def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[10:29], start=10) if x % -61 == 0 or x % -64 == 0))