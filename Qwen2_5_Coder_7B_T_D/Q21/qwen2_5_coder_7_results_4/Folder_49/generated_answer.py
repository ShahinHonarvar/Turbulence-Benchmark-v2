def all_ints_div_by_num(lst):
    return [n for i, n in enumerate(lst) if i >= 30 and i <= 300 and (n % 5 == 0)]