def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 13 and i <= 91 and (x % -65 == 0 or x % -62 == 0)))