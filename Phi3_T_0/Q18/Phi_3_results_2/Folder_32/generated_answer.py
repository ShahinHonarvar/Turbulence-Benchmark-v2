def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[25:96] if x % 51 == 0 or x % 77 == 0))