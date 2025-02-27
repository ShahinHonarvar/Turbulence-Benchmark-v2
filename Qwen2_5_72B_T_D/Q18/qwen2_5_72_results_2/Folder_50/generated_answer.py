def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[46:92] if x % 67 == 0 or x % 15 == 0)) if len(lst) > 91 else 0