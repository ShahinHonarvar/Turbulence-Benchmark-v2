def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:9]) if x % -3 == 0 or x % 8 == 0))