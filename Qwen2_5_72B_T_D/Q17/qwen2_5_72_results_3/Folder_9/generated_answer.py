def all_ints_div_by_both_two_nums(lst):
    result = [x for i, x in enumerate(lst) if 70 <= i <= 200 and x % 3 == 0 and (x % -300 == 0)]
    return result