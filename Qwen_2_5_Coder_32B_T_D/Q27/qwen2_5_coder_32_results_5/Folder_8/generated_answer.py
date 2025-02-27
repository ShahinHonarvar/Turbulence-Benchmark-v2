def insert_after_index(lst):
    if 57 < len(lst):
        lst = lst[:58] + [76] + lst[58:]
    return lst