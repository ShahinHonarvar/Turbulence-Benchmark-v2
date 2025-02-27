def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 48 and i < 62 and (num % 28 != 0)]