def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 86 and i <= 89 and (x % -61 == 0 or x % -79 == 0)))