def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[81:90], start=81) if x % 56 == 0 or x % 68 == 0))