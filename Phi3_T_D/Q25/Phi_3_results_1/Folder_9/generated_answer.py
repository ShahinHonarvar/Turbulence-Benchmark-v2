def insert_at_index(lst):
    if len(lst) < 66:
        lst.append(45)
    else:
        lst.insert(66, 45)
    return lst