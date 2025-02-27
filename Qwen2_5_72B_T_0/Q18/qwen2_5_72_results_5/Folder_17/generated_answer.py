def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[81:90] if x % 56 == 0 or x % 68 == 0))