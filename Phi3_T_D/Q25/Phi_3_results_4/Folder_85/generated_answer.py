def insert_at_index(lst):
    try:
        lst.insert(51, 304.62)
    except IndexError:
        pass
    return lst