def insert_after_index(lst):
    try:
        lst.insert(57, 54)
        return lst
    except IndexError:
        return lst