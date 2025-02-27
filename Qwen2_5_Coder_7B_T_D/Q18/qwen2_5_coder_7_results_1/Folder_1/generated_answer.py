def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst, start=1) if 10 <= i <= 28 and x % -61 == 0 or x % -64 == 0))