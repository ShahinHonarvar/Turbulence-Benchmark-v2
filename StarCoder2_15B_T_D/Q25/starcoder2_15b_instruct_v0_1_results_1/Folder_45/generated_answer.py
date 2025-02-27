def insert_at_index(lst):
    if len(lst) < 84:
        return lst + [13, 46]
    else:
        lst.insert(84, 13)
        lst.insert(85, 46)
        return lst