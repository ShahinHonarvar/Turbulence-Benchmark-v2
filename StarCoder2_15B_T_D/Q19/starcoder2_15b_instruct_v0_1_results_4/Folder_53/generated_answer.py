def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 199 and i < 201 and (num % -200 != 0)]