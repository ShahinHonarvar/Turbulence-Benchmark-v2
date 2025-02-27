def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 15 and i < 57 and (num % 86 != 0)]