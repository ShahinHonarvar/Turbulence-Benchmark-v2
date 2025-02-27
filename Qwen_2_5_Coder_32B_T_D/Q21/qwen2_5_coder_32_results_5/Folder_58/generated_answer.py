def all_ints_div_by_num(lst):
    if len(lst) < 619:
        return []
    return [x for x in lst[255:619] if x % 965 == 0]