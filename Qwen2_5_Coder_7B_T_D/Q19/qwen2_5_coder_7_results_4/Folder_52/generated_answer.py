def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 50 and i < 92 and (num % 16 != 0)]