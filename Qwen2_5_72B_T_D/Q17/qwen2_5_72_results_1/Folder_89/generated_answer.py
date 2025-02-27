def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[28:97], start=28) if x % 90 == 0 and x % 97 == 0]