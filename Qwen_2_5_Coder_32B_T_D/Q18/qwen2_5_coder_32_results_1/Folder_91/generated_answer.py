def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:5]) if i >= 0 and i <= 4 and (x % 8 == 0 or x % -3 == 0)))