def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[90:98] if x % 13 == 0 or x % 35 == 0)) if len(lst) > 97 else 0