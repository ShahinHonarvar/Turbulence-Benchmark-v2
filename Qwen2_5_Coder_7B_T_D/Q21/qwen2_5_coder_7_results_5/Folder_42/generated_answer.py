def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 31 and i <= 92 and (num % 20 == 0)]