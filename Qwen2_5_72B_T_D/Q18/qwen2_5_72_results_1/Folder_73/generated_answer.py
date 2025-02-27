def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[81:87], start=81) if x % -33 == 0 or x % -62 == 0))