def all_pos_ints_inclusive(lst):
    try:
        return [x for x in lst[42:69] if x > 0]
    except IndexError:
        return []