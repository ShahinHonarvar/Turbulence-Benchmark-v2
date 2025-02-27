def insert_after_index(lst):
    if len(lst) < 63:
        return lst
    else:
        lst.insert(63, 51)
        return lst