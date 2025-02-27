def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 2 and i < 7 and (num % 8 != 0)]