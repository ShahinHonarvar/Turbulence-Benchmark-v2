def insert_at_index(lst):
    if len(lst) >= 73:
        lst.insert(73, 418.88)
    else:
        return lst + [418.88]
    return lst