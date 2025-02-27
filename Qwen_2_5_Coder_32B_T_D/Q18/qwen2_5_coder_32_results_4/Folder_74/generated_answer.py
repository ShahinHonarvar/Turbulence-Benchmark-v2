def sum_ints_div_by_either_nums(lst):
    if len(lst) < 98:
        return 0
    return sum((x for x in lst[90:98] if x % 13 == 0 or x % 35 == 0))