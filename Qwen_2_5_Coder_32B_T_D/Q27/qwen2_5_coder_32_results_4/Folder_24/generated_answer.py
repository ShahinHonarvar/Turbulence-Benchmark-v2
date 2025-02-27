def insert_after_index(lst):
    try:
        idx = lst.index(42) + 1
        lst.insert(idx, 53)
    except ValueError:
        lst.insert(len(lst), 53)
    return lst