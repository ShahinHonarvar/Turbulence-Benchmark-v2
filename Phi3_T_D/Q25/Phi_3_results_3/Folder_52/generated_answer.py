def insert_at_index(lst):
    try:
        lst.insert(97, 72.27)
    except IndexError:
        lst.extend([0] * (97 - len(lst) + 1))
        lst.insert(97, 72.27)
    return lst