def insert_after_index(lst):
    idx94 = lst.index(94) if 94 in lst else None
    return lst[:idx94 + 1] + [93] + lst[idx94 + 1:] if idx94 is not None else lst