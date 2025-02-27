def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 19 and i < 69 and (num % 97 != 0)]