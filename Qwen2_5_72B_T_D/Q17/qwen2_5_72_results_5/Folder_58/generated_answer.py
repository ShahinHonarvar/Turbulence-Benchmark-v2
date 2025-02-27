def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[240:902], start=240) if x % 546 == 0 and x % 709 == 0]