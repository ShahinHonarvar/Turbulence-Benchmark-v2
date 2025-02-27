def insert_after_index(lst):
    try:
        lst.insert(71, 76)
    except IndexError:
        lst.append(76)
    return lst