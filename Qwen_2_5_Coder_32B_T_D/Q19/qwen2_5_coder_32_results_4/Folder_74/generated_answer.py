def all_ints_not_div_by_num(lst):
    if len(lst) > 94:
        return [x for x in lst[93:95] if x % 57 != 0]
    return []