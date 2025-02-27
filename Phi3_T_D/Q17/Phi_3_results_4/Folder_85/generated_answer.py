def all_ints_div_by_both_two_nums(lst):
    filtered_list = [x for x in lst[1:9] if x % -9 == 0 and x % -3 == 0]
    return filtered_list