def insert_after_index(lst):
    try:
        index = lst.index(99)
    except ValueError:
        return lst
    else:
        lst.insert(index + 1, 99)
        return lst