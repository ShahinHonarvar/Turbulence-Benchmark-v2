def insert_at_index(lst):
    if len(lst) < 35:
        return lst[:35] + [88] + lst[35:]
    else:
        return lst[:35] + [88] + lst[35:]