def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 30 <= i <= 200 and (x % 115 == 0 or x % -115 == 0)))