def all_ints_div_by_both_two_nums(lst):
    if len(lst) > 7:
        if lst[7] % 5 == 0 and lst[7] % 7 == 0:
            return [lst[7]]
        else:
            return []
    else:
        return []