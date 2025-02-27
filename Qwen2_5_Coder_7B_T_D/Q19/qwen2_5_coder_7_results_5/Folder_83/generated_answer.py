def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 90 and i < 200 and (num % -31 != 0)]