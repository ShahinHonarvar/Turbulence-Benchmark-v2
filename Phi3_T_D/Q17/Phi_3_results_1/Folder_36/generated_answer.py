def all_ints_div_by_both_two_nums(lst):
    filtered_list = [x for x in lst[299:383] if x % 858 == 0 and x % 952 == 0]
    return filtered_list