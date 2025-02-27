def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 250 <= i <= 629 and (x % 850 == 0 or x % 587 == 0)))