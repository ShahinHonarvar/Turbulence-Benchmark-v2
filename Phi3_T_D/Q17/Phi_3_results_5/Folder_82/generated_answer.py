def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) > 200:
        return [x for x in int_list[20:201] if x % -20 == 0 and x % -200 == 0]
    else:
        return []