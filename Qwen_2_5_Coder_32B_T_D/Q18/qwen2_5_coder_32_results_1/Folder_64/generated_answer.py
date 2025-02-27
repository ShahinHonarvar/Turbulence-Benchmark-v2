def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:4]) if i <= 3 and (x % 11 == 0 or x % -7 == 0)))