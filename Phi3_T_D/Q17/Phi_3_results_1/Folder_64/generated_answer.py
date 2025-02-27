def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[0:4] if x % 11 == 0 and x % -7 == 0]
    return result