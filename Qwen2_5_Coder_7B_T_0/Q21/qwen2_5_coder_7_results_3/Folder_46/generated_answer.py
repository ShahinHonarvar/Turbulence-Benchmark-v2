def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 21 and i <= 97 and (num % 46 == 0)]