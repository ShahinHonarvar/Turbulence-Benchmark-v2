def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 81 <= idx <= 86 and (i % -33 == 0 or i % -62 == 0)))