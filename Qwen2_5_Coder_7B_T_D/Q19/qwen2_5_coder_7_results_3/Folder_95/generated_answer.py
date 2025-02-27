def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 38 and i < 52 and (num % -41 != 0)]