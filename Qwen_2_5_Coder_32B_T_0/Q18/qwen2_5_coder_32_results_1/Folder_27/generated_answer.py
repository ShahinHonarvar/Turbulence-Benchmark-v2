def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 20 <= i <= 35 and (x % -36 == 0 or x % -89 == 0)))