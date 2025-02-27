def insert_after_index(lst):
    if len(lst) >= 64:
        lst = lst[:64] + [99] + lst[64:]
    return lst