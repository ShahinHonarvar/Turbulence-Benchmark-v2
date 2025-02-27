def insert_at_index(lst):
    lst_length = len(lst)
    return lst[:62] + [19, 13] + lst[62:] if lst_length >= 62 else lst + [19, 13]