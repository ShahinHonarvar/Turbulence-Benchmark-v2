def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 43 and i < 77 and (num % 84 != 0)]