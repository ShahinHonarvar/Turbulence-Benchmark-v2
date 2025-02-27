def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[42:43] if x % 15 == 0 or x % 87 == 0))