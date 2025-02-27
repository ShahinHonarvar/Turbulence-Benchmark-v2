def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:11] if x % 10 == 0 or x % 100 == 0))