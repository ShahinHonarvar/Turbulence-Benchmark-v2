def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[42:44] if x % 15 == 0 and x % 87 == 0]
    return result