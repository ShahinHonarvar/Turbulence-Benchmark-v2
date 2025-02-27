def sum_ints_div_by_either_nums(lst):
    sum_of_divisibles = sum((x for x in lst[48:60] if x % 88 == 0 or x % 58 == 0))
    return sum_of_divisibles