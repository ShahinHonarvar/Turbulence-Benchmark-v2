def insert_after_index(lst):
    if len(lst) > 74:
        lst = lst[:75] + [51, 29] + lst[75:]
    return lst