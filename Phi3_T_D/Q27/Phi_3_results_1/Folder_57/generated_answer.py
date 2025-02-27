def insert_after_index(lst):
    try:
        lst.insert(lst.index(80) + 1, 80)
    except ValueError:
        lst.insert(100, 80)
    return lst