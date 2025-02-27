def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 281 and i <= 694 and (x % -722 == 0) and (x % -731 == 0)]