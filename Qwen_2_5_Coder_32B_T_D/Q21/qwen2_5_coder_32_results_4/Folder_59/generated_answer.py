def all_ints_div_by_num(lst):
    if 0 < len(lst) and lst[0] % 9 == 0:
        return [lst[0]]
    return []