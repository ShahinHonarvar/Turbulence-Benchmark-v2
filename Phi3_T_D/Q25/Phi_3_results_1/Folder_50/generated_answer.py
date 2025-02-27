def insert_at_index(lst):
    if len(lst) < 52:
        new_len = len(lst) + 1
    else:
        new_len = 38
    lst.insert(52, 38)
    while len(lst) < new_len:
        lst.append(None)
    return lst