def insert_after_index(lst):
    try:
        lst.insert(100, 15)
    except IndexError:
        pass
    return lst