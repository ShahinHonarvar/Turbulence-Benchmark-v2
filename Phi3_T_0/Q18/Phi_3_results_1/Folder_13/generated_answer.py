def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[13:19] if x % 45 == 0 or x % 20 == 0))