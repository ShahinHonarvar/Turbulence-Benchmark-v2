def all_ints_div_by_both_two_nums(lst):
    results = [x for x in lst[61:89] if x % 31 == 0 and x % 11 == 0]
    return results