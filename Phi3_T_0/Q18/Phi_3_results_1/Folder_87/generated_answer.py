def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[18:53] if x % 15 == 0 or x % 57 == 0))