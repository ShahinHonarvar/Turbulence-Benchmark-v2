def all_ints_div_by_num(lst):
    if len(lst) > 81:
        return [i for i in lst[66:82] if i % 77 == 0]
    return []