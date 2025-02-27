def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 36 and i < 85 and (num % -27 != 0)]