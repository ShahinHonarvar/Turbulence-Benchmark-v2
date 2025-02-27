def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if (i >= 68 and i <= 99) and (x % -37 == 0 or x % -26 == 0)))