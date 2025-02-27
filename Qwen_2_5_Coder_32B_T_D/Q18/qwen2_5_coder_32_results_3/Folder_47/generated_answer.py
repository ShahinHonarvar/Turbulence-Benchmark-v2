def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 42 <= i <= 87 and (x % -90 == 0 or x % -74 == 0)))