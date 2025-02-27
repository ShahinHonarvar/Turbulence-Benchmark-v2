def insert_after_index(lst):
    if len(lst) <= 95:
        lst.append(43)
    else:
        lst.insert(96, 43)
    return lst