def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 60 <= i <= 200 and (x % 9 == 0 or x % 11 == 0)))