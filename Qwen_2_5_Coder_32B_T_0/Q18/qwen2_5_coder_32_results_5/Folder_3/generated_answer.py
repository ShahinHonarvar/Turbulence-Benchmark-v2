def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 38 <= i <= 52 and (x % -41 == 0 or x % -47 == 0)))