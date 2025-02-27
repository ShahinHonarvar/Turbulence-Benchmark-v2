def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 299 and i <= 382 and (x % 858 == 0 or x % 952 == 0)))