def insert_after_index(lst):
    try:
        lst.insert(99, 99)
    except IndexError:
        lst.append(99)
    return lst