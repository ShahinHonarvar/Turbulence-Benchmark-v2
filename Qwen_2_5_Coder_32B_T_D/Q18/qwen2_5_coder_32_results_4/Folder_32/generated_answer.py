def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 25 <= i <= 95 and (x % 51 == 0 or x % 77 == 0)))