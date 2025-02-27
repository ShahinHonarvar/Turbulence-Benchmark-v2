def insert_at_index(lst):
    if len(lst) < 85:
        return lst[:85] + [27] + lst[85:]
    return lst[:85] + [27] + lst[85:]