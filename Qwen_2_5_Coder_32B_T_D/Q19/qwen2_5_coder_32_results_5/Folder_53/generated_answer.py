def all_ints_not_div_by_num(lst):
    if len(lst) <= 201:
        return []
    return [x for i, x in enumerate(lst[199:201]) if x % -200 != 0]