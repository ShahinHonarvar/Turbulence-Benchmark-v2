def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 154 <= i <= 798 and (x % 275 == 0 or x % 580 == 0)))