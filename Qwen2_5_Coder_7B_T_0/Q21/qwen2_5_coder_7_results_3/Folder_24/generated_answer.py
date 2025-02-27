def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 12 and i <= 77 and (num % -19 == 0)]