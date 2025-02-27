def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 45 and i < 72 and (num % 93 != 0)]