def insert_after_index(lst):
    try:
        index = lst.index(99)
        lst.insert(index + 1, 99)
    except ValueError:
        pass
    return lst