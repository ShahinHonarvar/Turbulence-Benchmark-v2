def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[0:10:1] if x % 6 == 0 and x % -3 == 0]
    return result