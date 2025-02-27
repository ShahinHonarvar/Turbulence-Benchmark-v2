def all_ints_div_by_both_two_nums(lst):
    divisible = [x for x in lst[315:935] if x % -897 == 0 and x % -556 == 0]
    return divisible