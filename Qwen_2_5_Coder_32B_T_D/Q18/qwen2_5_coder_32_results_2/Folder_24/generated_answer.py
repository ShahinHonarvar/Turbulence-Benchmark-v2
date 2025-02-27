def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 29 <= i <= 53 and (x % -68 == 0 or x % -85 == 0)))