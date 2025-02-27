def all_ints_not_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if idx > 0 and idx < 5 and (num % 8 != 0)]