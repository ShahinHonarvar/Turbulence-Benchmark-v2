def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[13:92], start=13) if x % -65 == 0 or x % -62 == 0))