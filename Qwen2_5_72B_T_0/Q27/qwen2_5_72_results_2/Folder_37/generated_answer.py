def insert_after_index(lst):
    if len(lst) > 35:
        lst.insert(36, 88)
    else:
        lst.append(88)
    return lst