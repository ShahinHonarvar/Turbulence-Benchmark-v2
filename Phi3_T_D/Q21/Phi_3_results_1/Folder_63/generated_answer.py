def all_ints_div_by_num(lst):
    if len(lst) > 54:
        return [x for x in lst[50:55] if x % 84 == 0]
    return []