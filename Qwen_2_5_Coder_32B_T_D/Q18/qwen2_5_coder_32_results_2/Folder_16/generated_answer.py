def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 55 <= idx <= 80 and (i % 22 == 0 or i % 32 == 0)))