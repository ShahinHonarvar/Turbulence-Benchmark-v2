def all_pos_ints_inclusive(lst):
    if len(lst) < 24:
        return []
    filtered_lst = list(filter(lambda x: x > 0, lst[23:24]))
    return filtered_lst