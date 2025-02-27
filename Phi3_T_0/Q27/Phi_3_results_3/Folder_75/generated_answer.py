def insert_after_index(lst):
    try:
        lst.insert(lst.index(99) + 1, 99)
    except ValueError:
        lst.append(99)
    return lst