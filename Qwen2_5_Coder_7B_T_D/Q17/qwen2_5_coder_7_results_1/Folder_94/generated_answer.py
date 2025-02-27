def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if x % -53 == 0 and x % -91 == 0 and (93 <= i <= 94)]