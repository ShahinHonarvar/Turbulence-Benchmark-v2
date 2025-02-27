def insert_at_index(lst):
    if len(lst) < 8:
        lst.append([3, 8])
    else:
        lst.insert(8, [3, 8])
    return lst