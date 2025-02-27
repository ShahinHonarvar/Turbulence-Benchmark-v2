def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[68:100], start=68) if x % -37 == 0 and x % -26 == 0]