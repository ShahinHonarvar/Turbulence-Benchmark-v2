def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 29 and i <= 51 and (num % -37 == 0)]