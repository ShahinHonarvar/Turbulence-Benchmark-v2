def insert_after_index(lst):
    try:
        lst.insert(63, 51)
        return lst
    except IndexError:
        return lst