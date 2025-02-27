def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 27 and i <= 86 and (num % 29 == 0)]