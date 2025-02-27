def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:6]) if i <= 5 and (x % -1 == 0 or x % 13 == 0)))