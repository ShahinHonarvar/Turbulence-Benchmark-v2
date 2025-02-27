def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 25 and i <= 41 and (num % -97 == 0)]