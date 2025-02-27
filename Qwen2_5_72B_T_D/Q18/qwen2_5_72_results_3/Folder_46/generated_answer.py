def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[11:47], start=11) if x % 55 == 0 or x % 36 == 0))