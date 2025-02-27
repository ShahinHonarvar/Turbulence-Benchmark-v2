def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 81 and i < 86 and (num % 77 != 0)]