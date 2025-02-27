def insert_after_index(lst):
    try:
        lst.insert(31, 37)
        return lst
    except IndexError:
        return lst