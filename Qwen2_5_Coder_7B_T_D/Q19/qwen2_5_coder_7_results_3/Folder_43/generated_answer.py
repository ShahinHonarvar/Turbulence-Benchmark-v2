def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 16 and i < 87 and (num % -15 != 0)]