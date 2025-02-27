def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:3] if x % -2 == 0 or x % 3 == 0))