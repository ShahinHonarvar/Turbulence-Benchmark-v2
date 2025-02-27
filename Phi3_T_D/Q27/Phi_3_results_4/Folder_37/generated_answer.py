def insert_after_index(lst):
    try:
        lst.insert(36, 88)
        return lst
    except IndexError:
        return lst