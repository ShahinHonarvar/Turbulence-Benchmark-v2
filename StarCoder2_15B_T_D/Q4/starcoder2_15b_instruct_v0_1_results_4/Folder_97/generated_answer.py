def all_pos_ints_exclusive(lst):
    try:
        return [x for x in lst[20:93] if x > 0]
    except IndexError:
        return []